from django.urls import re_path, include, path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path(r'^i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    re_path(r'^', include('wedding.urls')),
    re_path(r'^', include('guests.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path('^accounts/', include('django.contrib.auth.urls'))
)