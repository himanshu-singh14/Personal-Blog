from django.db import models


# This model is for our contact page in which we take input from users and store in database
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    content = models.TextField()
    timeStamp = models.DateTimeField(blank=True , auto_now_add=True)

    def __str__(self):
        return self.name
    
