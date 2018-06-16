from django.db import models
import datetime	

# Create your models here.

class User(models.Model):
	actual_name = models.CharField(max_length=30)
	user_name = models.CharField(max_length=20)
	user_password = models.CharField(max_length=50)
	user_email = models.EmailField(
    	verbose_name ='email address',
        max_length=50,
        unique=True,
    )
	active = models.BooleanField(default=True)

class userNotes(models.Model):
	note_title =  models.CharField(max_length=50)
	note_detail = models.CharField(max_length=200)
	due_date = models.DateField()
	created_date = models.DateField(default=datetime.date.today, blank=True) 
	high_imp = models.BooleanField(default=False)
	status = models.BooleanField(default=False)
	usr_name = models.ForeignKey(User, on_delete=models.CASCADE)
	
	
	