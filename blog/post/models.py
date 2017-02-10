from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=40, blank=True)
	content = models.TextField(blank=True)
	image = models.ImageField()
	date_time = models.DateTimeField(auto_now=True, blank=True)
	author = models.CharField(max_length=40)
	likes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	post_id = models.ForeignKey(Post)
	comment_name = models.CharField(max_length=40)
	comment_content = models.CharField(max_length=120)

	def __unicode__(self):
		return self.comment_name
