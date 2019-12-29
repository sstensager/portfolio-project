from django.db import models

# Create your models here.

class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=200)
	pub_date = models.DateField()
	body = models.CharField(max_length=1000)



# title
#  pub_date
#  body
#  image

# Create a blog models

# Add the blog app to the settings

# Create a migration

# migrate

# add to the admin