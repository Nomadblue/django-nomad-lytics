from celery import task


@task.task(ignore_result=True)
def send_mixpanel_track_from_celery(event):
    from nomadlytics.utils import send_mixpanel_track
    return send_mixpanel_track(event)

