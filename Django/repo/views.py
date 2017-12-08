from django.shortcuts import render
from django.views.generic.list import ListView
from .models import RepoInformation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
from django.views import View

class IndexView(ListView):
    def get(self, request):
    	model = RepoInformation
    	paginate_by = 10
    	info = RepoInformation.objects.order_by('name')
    	j = ''
    	for i in info:
    		url_temp = str(i.url).split("', u'")
    		if len (url_temp) >= 1:
    			if len(url_temp) == 1:
    				pass
    			elif len(url_temp) == 2:
    				print url_temp
    				#url_0_1 = url_0.split("']")[0] 
    				#	i.url = url_0_1
    				#	i.save()
    				#if "']" in url_temp[0].split("[u'")[1]:
    				#	url_0_1 = url_0.split("']")[0] 
    				#url_t = url_temp[1]
    				#if "']" in url_t:
    				#	url_1 = url_t.split("']")[0]
    				#	#print url_1
    			elif len(url_temp) == 3:
    				#print url_temp[1]
    				pass
    			else:
    				print len(url_temp)
    	return render(request, 'repo/index.html', {'info':info})
        
class DetailView(View):
	def get(self, request, name):
		info = RepoInformation.objects.filter(name=name)
		print len(info)
		return render(request, 'repo/details.html', {'info':info})