from django.db import models

# Create your models here.

class url_links(models.Model):

	link_id = models.AutoField(primary_key=True)
	links = models.CharField(max_length=10000000000)
	short_link = models.CharField(max_length=100000)

	