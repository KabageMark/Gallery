from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns=[
    url(r'^$',views.Gallery,name = 'gallery'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(\w+)', views.display_location,name='display_location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)     