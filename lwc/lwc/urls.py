from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'joins.views.home', name='home'),  # $ - ends the string
    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),
    # url(r'^blog/', include('blog.urls')),

)
urlpatterns += staticfiles_urlpatterns()
