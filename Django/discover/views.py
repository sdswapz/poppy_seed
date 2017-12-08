from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import UploadDocuments
from android.models import AndroidDocumentsMagic, InformationAboutPacker, AndroidInformation
from django.views import View
from android.axmlparser.apk import APK, CheckMagic
import hashlib
from django.core.exceptions import ObjectDoesNotExist

def get_dict():
	dict_r = CheckMagic()
	dict_rule = dict_r.magic_info()
	return dict_rule

class UploadView(View):
	def get(self, request):
		self.templateName = "discover/upload.html"
		return render(request, self.templateName)
	
	def post(self, request):
		self.files = request.FILES.getlist('file', False)
		self.scanned = False
		for file in self.files:
			self.buff = file.read()
			if b'\x00' in self.buff:
				try: 
					hashPresent = AndroidDocumentsMagic.objects.get(apphash = (hashlib.sha1(self.buff).hexdigest()))
					print 'File Exists in the DB: ', file
				except ObjectDoesNotExist:
					print 'File Does Not Exists in the DB: ', file
					UploadView.get_magic(self) 
				if self.scanned and self.xml:
					upload_info = AndroidDocumentsMagic(magicfile = self.magic, filename = file, ftype = self.fname, apphash = hashlib.sha1(self.buff).hexdigest()).save()
					android_info = AndroidInformation(appid = hashlib.sha1(self.buff).hexdigest(), description = self.xml, packerinfo = self.packerDetails, filenames = self.fileNames).save()	
		return render(request, "discover/details.html")

	def get_magic(self):
		scanMagic = get_dict()
		self.packerDetails = []
		self.fileNames = []
		magic = self.buff[:4]
		self.magic = magic
		for key in scanMagic.keys():
			if magic in scanMagic[key]:
				self.scanned = True
				UploadView.get_apk(self, key)

	def get_apk(self, key):
		apk = APK()
		self.file = file
		raw = self.buff
		if 'apk' in key and b'AndroidManifest.xml' in raw:
			self.fname = 'Android Filetype'
			info, self.xml, self.fileNames = apk.scan_apk(raw)
			self.packerDetails.append(info)
		elif 'dex' in key:
			self.fname = 'DEX Filetype'
			dexobj = apk.scan_dex(raw)
		elif 'axml' in key: 
			self.fname = 'Android Manifest File'
			self.xml = apk.scan_axml(raw)
			self.fileNames.append('AndroidManifest.xml')
		elif 'arsc' in key:
			self.fname = 'Resource File'
			arscobj = apk.scan_arsc(raw)
		else:
			self.fname = 'ELF or SO library'
		
class AboutView(View):
	def get(self, request):
		return render(request, 'discover/about.html')
