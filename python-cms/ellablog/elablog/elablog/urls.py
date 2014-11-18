from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# register apps for Django admin and let the apps do any initialization they need
from ella.utils.installedapps import call_modules
call_modules(('admin','register',))

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elablog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    # serve media files
    (r'^%s/(?P<path>.*)$' settings.MEDIA_URL, 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    # run Django admin
    (r'^admin/', include(admin.site.urls)),

    # enable Ella
    (r'^', include('ella.core.urls')),
) + staticfiles_urlpatterns()
