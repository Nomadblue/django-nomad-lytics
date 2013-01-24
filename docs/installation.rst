============
Installation
============

Dependencies
============

* `libsaas`_: django-nomadlytics uses this app to push the events to track
  to the different services.
* `django-celery`_ (optional): if you want to track events asynchronously (recommended)

.. _libsaas: https://github.com/ducksboard/libsaas
.. _django-celery: https://github.com/celery/django-celery

Initial setup
=============

The package is listed in the `Python Package Index`_. You can use your favorite
package manager like ``easy_install`` or ``pip``::

    pip install django-nomadlytics

Or, you can clone the latest development code from its repository::

    git clone git@github.com:Nomadblue/django-nomadlytics.git

.. _Python Package Index: http://pypi.python.org/pypi/django-nomadlytics/

Add ``nomadlytics`` to the ``INSTALLED_APPS`` setting of your ``settings.py``::

    INSTALLED_APPS = (
        ...
        'nomadlytics',
    )

