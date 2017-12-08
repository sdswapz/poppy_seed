from __future__ import unicode_literals
from django.db import models

class RepoInformation(models.Model):
	name = models.CharField(max_length=100, unique=True, blank=False)
	mname = models.CharField(max_length=100, blank=True)
	mtype = models.CharField(max_length=100,  blank=True)
	date_found = models.CharField(max_length=100, blank=True)
	description = models.TextField(max_length=5000,  blank=True)
	url = models.URLField()
	num_of_binary = models.PositiveSmallIntegerField()
	num_of_dec = models.PositiveSmallIntegerField()
	num_of_source = models.PositiveSmallIntegerField()
	binary_path = models.CharField(max_length=100, blank=True)
	dec_path = models.CharField(max_length=100, blank=True)
	og_source_path = models.CharField(max_length=100, blank=True)

	def get_path(filename):
		return filename
