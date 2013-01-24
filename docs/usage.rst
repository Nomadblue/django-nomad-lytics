======
Usage
======

Here is an snippet of code to see how easy is to trigger an event
to Mixpanel from anywhere in your project::

    from nomadlytics.utils import send_mixpanel_track

    event = settings.NOMADLYTICS_EVENTS.get('send_pic')
    event['props']['recipient_num'] = '<num_of_recipients_value_here>'  # This line is optional, only if you have props to configure
    send_mixpanel_track(event)

You can also the `celery`_ wrapper function to push asynchronously::

    from nomadlytics.tasks import send_mixpanel_track_from_celery

    event = settings.NOMADLYTICS_EVENTS.get('send_pic')
    event['props']['recipient_num'] = '<num_of_recipients_value_here>'  # This line is optional, only if you have props to configure
    send_mixpanel_track_from_celery(event)

.. _`celery`: http://celeryproject.org/

