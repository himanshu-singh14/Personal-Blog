from django.shortcuts import render, HttpResponse
from .models import Post


# This API is for home page of blog app
def blogHome(request):
	# Here we are going to fetch all posts from database of Post table
	allPosts = Post.objects.all()
	mydict = {'allPosts':allPosts}
	return render(request, 'blog/blogHome.html', mydict)

# This API is for individual post
def blogPost(request, slug):
	# Here we send slug or string to blockPost Page from Home page
	# slug contain only one items. Hence, use first()
	post = Post.objects.filter(slug=slug).first()
	mydict = {'post':post}
	return render(request, 'blog/blogPost.html',mydict)