from django.contrib.auth import admin
from django.templatetags.static import static
from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
from django.conf import settings
from django.conf.urls.static import staticurl
patterns = [
path('admin/', admin.site.urls),
    ...]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
