from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    url(r'^$', TemplateView.as_view(template_name="pre.html")),
    url(r'^post$', TemplateView.as_view(template_name="post.html")),
    url(r'^error$', TemplateView.as_view(template_name="error.html")),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
