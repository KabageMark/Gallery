from django.conf.urls import url,include
from django.conf import settings
from .import views

urlpatterns=[
    url(r'^$',views.Gallery,name = 'gallery'),
    ] 