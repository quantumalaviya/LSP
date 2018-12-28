from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # to auth
	path('signup/', include('signup.urls')), #to signup
	path('', TemplateView.as_view(template_name='home.html'), name='home'), #the homepage
]