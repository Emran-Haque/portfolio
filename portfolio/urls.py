"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# View for serving robots.txt
def robots_txt(request):
    with open(BASE_DIR / 'robots.txt', 'r') as f:
        return HttpResponse(f.read(), content_type='text/plain')

# View for serving sitemap.xml
def sitemap_xml(request):
    with open(BASE_DIR / 'sitemap.xml', 'r') as f:
        return HttpResponse(f.read(), content_type='application/xml')

# View for serving llms.txt
def llms_txt(request):
    with open(BASE_DIR / 'llms.txt', 'r') as f:
        return HttpResponse(f.read(), content_type='text/plain')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', robots_txt, name='robots'),
    path('sitemap.xml', sitemap_xml, name='sitemap'),
    path('llms.txt', llms_txt, name='llms'),
    path('', include('home.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
