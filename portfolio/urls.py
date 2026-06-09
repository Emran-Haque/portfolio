from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def robots_txt(request):
    content = "User-agent: *\nAllow: /\n"
    return HttpResponse(content, content_type='text/plain')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', robots_txt),
    path('api/', include('home.urls')),
    path('api/blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
