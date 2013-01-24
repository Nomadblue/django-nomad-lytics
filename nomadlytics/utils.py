from django.conf import settings

from libsaas.services import mixpanel


def send_mixpanel_track(event):
    if getattr(settings, 'NOMADLYTICS_ENABLED'):
        basic = mixpanel.Mixpanel(token=settings.MIXPANEL_TOKEN, api_key=settings.MIXPANEL_API_KEY, api_secret=settings.MIXPANEL_API_SECRET)
        basic.track(event.get('name'), event.get('props'))

