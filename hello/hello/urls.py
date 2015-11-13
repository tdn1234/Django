from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'hello.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^users/', include('userprofile.urls')),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', {
                           'template_name': 'login_form.html'
                       })
                       )
if not settings.DEBUG:
    urlpatterns += patterns('', (r'^media/(.*)$',
                                 'django.views.static.serve',
                                 {'document_root': settings.MEDIA_ROOT}),
                            )
