django-assume
-------------

Django Assume is a simple, reusable Django app that allows administrators to
log in to other user accounts without having to provide a password. This can
be useful for investigating and troubleshooting problems related to specific
user accounts.

This app is intended for use with Django 1.3.

Suggestions and contributions are welcome. USE THIS APP AT YOUR OWN RISK!


Installation
------------

1.  Add `assume` to `settings.INSTALLED_APPS` and make sure that the
    `app_directories` template loader is enabled in your project.

2.  Add one of the custom authentication backends in `assume.backends` to
    `settings.AUTHENTICATION_BACKENDS`. For example:

        AUTHENTICATION_BACKENDS = (
            'assume.backends.AssumableModelBackend',
            'django.contrib.auth.backends.ModelBackend',
        )

3.  Include `assume.admin_urls` in your project's URL patterns:

        urlpatterns += patterns('',
            (r'^admin/', include('assume.admin_urls')),
        )

You should now see an "Assume" button near the top of each Change User form
in admin.