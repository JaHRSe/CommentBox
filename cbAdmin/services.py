import json
from django.core.exceptions import ValidationError
from commentbox.models import NotificationList
from .forms import CommentBoxForm, NotificationListForm


def getNotifyList():

    data = NotificationList.objects.latest()

    return data


def processAdminSave(data):
    try:
        data = json.loads(data);
        # Save comment box email address
        form = CommentBoxForm({'emailAddress': data['commentBoxEmail']})
        if form.is_valid():
            form.save()
        else:
            raise ValidationError(form.errors)

        # save notification list
        form = NotificationListForm({'notificationList': data['notificationList']})
        if form.is_valid():
            form.save()
        else:
            raise ValidationError(form.errors)

    except Exception as e:
        return False
    return True

