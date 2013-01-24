=============
Configuration
=============

Initial setup
=============

NOMADLYTICS_EVENTS
------------------

**Important**: You MUST configure this setting to get Nomadlytics running!

For each event that you want to track, you create a new name and properties inside
the ``NOMADLYTICS_EVENTS`` setting. For example, if we want to trigger event pushes
to Mixpanel for every picture one of our users sent to their list of friends::

    NOMADLYTICS_EVENTS = {
        'send_pic': {
            'name': 'Send pic',
            'props': {
                'num_of_recipients': '',
            },
        },
    }

In the example above, we have set an event called 'pic_sent' and we have added a
property 'num_of_recipients' that will count the number of friends that the picture
was sent to.

NOMADLYTICS_ENABLED 
-------------------

Default value: ``True``

This setting enables or disables sending the information to the services. For instance,
if you want to disable Nomadlytics::

    NOMADLYTICS_ENABLED = False

Services
========

Mixpanel
--------

Add the setings for you Mixpanel project::

    MIXPANEL_TOKEN='<your_project_token>'
    MIXPANEL_API_KEY='<your_project_api_key>'
    MIXPANEL_API_SECRET='<your_project_api_secret>'

