from django.conf.urls import patterns, url

urlpatterns = patterns('core',
    url(r'^$', 'views.home', name='home'),
)
