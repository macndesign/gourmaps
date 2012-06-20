from django.conf.urls import patterns, url

urlpatterns = patterns('core',
    url(r'^$', 'views.home', name='home'),
    url(r'^contact/$', 'views.contact', name='contact'),
    url(r'^data-contact-clear/$', 'views.data_contact_clear', name='data-contact-clear'),
    url(r'^contact-sent-clear/$', 'views.contact_sent_clear', name='contact-sent-clear'),
)
