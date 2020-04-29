from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User



# This API is for home page of home app
def home(request):
	return render(request, 'home/home.html')



# This API is for take input from contact page
def contact(request):
	if request.method == 'POST':
		# Fetch all items which is taken from contact page
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		content = request.POST['content']

		# Check the corrctness of creditials
		if len(name)<2 or len(email)<3 or len(phone)<5 or len(content)<4:
			# Shows message if above condition is true
			messages.error(request, 'Please fill the form correctly')
		else:
			messages.success(request, 'Your issue has been Successfully sent.')
			# Assign all credentials or inputs to items of models
			contact = Contact(name=name, email=email, phone=phone, content=content)
			# Save in database of model contact
			contact.save()
		return render(request, 'home/contact.html')
	else:
		return render(request, 'home/contact.html')



# This API is showing the about page
def about(request):
	return render(request, 'home/about.html')



# This API is for search the posts from all posts from given query in search box
def search(request):

	# Fetch the query by GET method
	query = request.GET['query']
	lenquery = len(query)

	# Fetch all posts from database which contain this query in title of that post 
	allPostsTitle = Post.objects.filter(title__icontains=query)
	# Fetch all posts from database which contain this query in content of that post
	allPostsContent = Post.objects.filter(content__icontains=query)
	# We want search all posts which contain that query in title or content. So, make it union
	allPosts = allPostsTitle.union(allPostsContent)

	# If allPosts contain None
	if not allPosts:
		messages.warning(request, 'Sorry, there is post available. Search for another one.')

	mydict = {'allPosts':allPosts, 'query':query, 'lenquery':lenquery}
	return render(request, 'home/search.html', mydict)



# This API is for handle the signup page
def handleSignUp(request):
	if request.method == 'POST':
		# Fetch all items which is taken from signup page
		username = request.POST['username']
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']

		# Check if both password are not same
		if pass1 != pass2:
			messages.error(request, 'Your password is not maching. Please signUp again')
			return redirect('home')

		# Create new user 
		newuser = User.objects.create_user(username, email, pass1)
		# Save both firs name and last name
		newuser.first_name = fname
		newuser.last_name = lname
		# Save in User in database
		newuser.save()
		messages.success(request, 'You account has been successfully Created')
		return redirect('home')
	else:
		return HttpResponse("404 - Not Found")



# This API is for handle the login page
def handleLogin(request):
	if request.method == "POST":
		# Fetch both username and password from login page
		loginusername = request.POST['loginusername']
		loginpassword = request.POST['loginpassword']
		# Check that user is authenticated or not if authenticated then return queryset of that user otherwise it return None
		user = authenticate(username=loginusername, password=loginpassword)

		if user is not None:
			# If is return user then login
			login(request, user)
			messages.success(request, 'You are Successfully Logged In')
			return redirect('home')
		else:
			messages.error(request, 'Invalid credentials, Please try again later')
			return redirect('home')
	else:
		return HttpResponse("404 - Not Found")


		
# This API is for handle the request for logout
def handleLogout(request):
	# Here it logout currnt user
	logout(request)
	messages.success(request, 'You are Successfully Logged Out')
	return redirect('home')