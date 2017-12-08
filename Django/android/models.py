from __future__ import unicode_literals
from django.db import models


class InformationAboutPacker(models.Model):
	packername = models.CharField(max_length=100, unique=True, blank=False)
	packerurl = models.URLField()
	resource = models.URLField()
	description = models.TextField(max_length=5000,  blank=True)

class AndroidDocumentsMagic(models.Model):
	magicfile = models.CharField(max_length=100)
	filename = models.CharField(max_length=400)
	ftype = models.CharField(max_length=100)
	apphash = models.CharField(max_length=100, unique=True, blank=False)

class AndroidInformation(models.Model):
	description = models.TextField(max_length=5000,  blank=True)
	filenames = models.TextField(max_length=5000,  blank=True)
	appid = models.CharField(max_length=100, unique=True, blank=False)
	packerinfo = models.CharField(max_length=100, blank=False)
	#appid = models.ForeignKey(AndroidDocumentsMagic, on_delete=models.CASCADE)
	#ahash = models.OneToOneField(AndroidDocumentsMagic, on_delete=models.CASCADE, primary_key=True,)