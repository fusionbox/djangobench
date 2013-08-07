from django.conf.urls import url, patterns, include

from widgybench.site import site

urlpatterns = patterns('',
    url('^widgy/', include(site.urls)),
)
