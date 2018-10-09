from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
# Create your views here.
from .models import KirrUrls


class HomeView(View):
	def get(self,request,*args,**kwargs):
		return render(request,"shortener/home.html",{})


	def post(self, request, *args, **kirr_redirect_viewwargs):
		print (request.POST)
		print (request.POST.get("url"))
		return render(request,"shortener/home.html",{})


class KirrCVView(View): 
	def get(self ,request, shortcode = None, *args ,**kwargs):
		obj = get_object_or_404(KirrUrls,shortcode=shortcode)
		return HttpResponseRedirect(obj.url)
	
			


# def kirr_redirect_view(request, shortcode = None, *args, **kwargs):

# 	obj = get_object_or_404(KirrUrls,shortcode=shortcode)
# 	return HttpResponseRedirect(obj.url)



# def kirr_redirect_view(request, shortcode = None, *args, **kwargs):

# 	obj = get_object_or_404(KirrUrls,shortcode=shortcode)
# 	# obj_url = obj.url
# 	# # try:
# 	# 	obj = KirrUrls.objects.get(shortcode=shortcode)
# 	# except:
# 	# 	obj = KirrUrls.objects.all().first()

# 	# obj_url = None
# 	# qs = KirrUrls.objects.filter(shortcode__iexact = shortcode)
# 	# if qs.exists():
# 	# 	obj = qs.first()
# 	# 	obj_url = obj.url

# 	return HttpResponse("hello world the url is {sc}".format(sc = obj.url))