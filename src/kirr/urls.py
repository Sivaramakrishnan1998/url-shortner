from django.conf.urls import url
from django.contrib import admin
from shortener.views import KirrCVView,HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+){6,15}$',KirrCVView.as_view()),	
 
]




   # (?P<slug>[/w-]+)

   # url(r'^2/(?P<shortcode>[\w-]+){6,15}}$',kirr_redirect_view),