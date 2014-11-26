from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^auth/user/(\d+)/assume/$', 'assume.views.assume_user', name='assume_user'),

)
