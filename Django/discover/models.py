from __future__ import unicode_literals
import os
from django.db import models

class UploadDocuments(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d', null=True, blank=True)
    
    def __str__(self):
        return "{}".format(self.file.name)
