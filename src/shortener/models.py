from django.conf import settings
from django.db import models 
from . utils import code_generator,create_shortcode

SHORTCODE_MAX = getattr(settings,"SHORTCODE_MAX",15)


class KirrUrlManager(models.Manager):
	def all(self,*args,**kwargs):
		qs_main = super(KirrUrlManager, self).all(*args,**kwargs)
		qs = qs_main.filter(active = True)
		return qs

	def refresh_shortcodes(self):
		qs = KirrUrls.objects.filter(id__gte=1)
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.shortcode)
			q.save()	
			new_codes += 1
		return "New Codes made: {i}".format(i=new_codes)


class KirrUrls(models.Model):
	url 	  = models.CharField(max_length = 220,)
	shortcode = models.CharField(max_length = SHORTCODE_MAX ,unique =True, blank = True)
	updated   = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	active    = models.BooleanField(default = False)

	objects = KirrUrlManager()
	some_random = KirrUrlManager()


	def save(self ,*args, **kwargs):
		# print("something")
		if self.shortcode== None or self.shortcode == "":
			self.shortcode = code_generator()
		super(KirrUrls, self).save(*args,**kwargs)		

	def __str__(self):
		return str(self.url)




