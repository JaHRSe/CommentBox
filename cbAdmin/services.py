import json
from django.core.exceptions import ValidationError
from commentbox.models import CommentBox, NotificationList,CbType
from .forms import CommentBoxForm, NotificationListForm


def getNotifyList(boxType):

    if NotificationList.objects.filter(type=boxType.value).exists():
        nl = NotificationList.objects.filter(type=boxType.value).latest()
        return nl.nl
    else:
        return []


def getCommentBoxEmail(boxType):

    address = None

    if CommentBox.objects.filter(type=boxType.value).exists():
        address = CommentBox.objects.filter(type=boxType.value).latest()

    if address:
        return address.emailAddress
    else:
        return ''


def processAdminSave(data):

    try:
        # Save comment box email address
        form = CommentBoxForm({'emailAddress': data['commentBoxEmail'], 'type': data['cbType'].name})

        if form.is_valid():
            form.save()
        else:
            raise ValidationError(form.errors)

        # save notification list
        form = NotificationListForm({'notificationList': data['notificationList'], 'type': data['cbType'].name})
        if form.is_valid():
            form.save()
        else:
            raise ValidationError(form.errors)

    except Exception as e:
        return False
    return True

