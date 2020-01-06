import json
from django.core.exceptions import ValidationError
from commentbox.models import CommentBox, NotificationList
from .forms import CommentBoxForm, NotificationListForm


def getNotifyList():

    if NotificationList.objects.exists():
        nl = NotificationList.objects.latest()
        return nl.notificationList
    else:
        return []


def getCommentBoxEmail():

    address = CommentBox.objects.latest()

    if address:
        return address.emailAddress
    else:
        return ''


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

