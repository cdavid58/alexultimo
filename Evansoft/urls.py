from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls import handler404, handler500
# from errors.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^post/', include('post.urls')),
    url(r'^social/', include('social.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^property/', include('property.urls')),
    url(r'^reservation/', include('reservation.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^settings/', include('settings.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# handler404 = handler404
# handler500 = handler500