from django.db import models
from django.contrib.postgres.fields import JSONField
from enum import Enum


class CbType(Enum):

    SS = 'SS'
    HRA = 'HRA'
    TS = 'TEST'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class CommentBox(models.Model):

    type = models.CharField(max_length=50,  choices=CbType.choices(), blank=True, default='')

    emailAddress = models.EmailField(blank=False, default='EADSCommentBox@gmail.com')

    created = models.DateTimeField(auto_now_add=True)

    class Meta:

        get_latest_by = 'created'


class NotificationList(models.Model):

    type = models.CharField(max_length=50, blank=True, default='')

    notificationList = JSONField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)

    @property
    def nl(self):
        if not self.notificationList:
            return []
        else:
            return self.notificationList

    class Meta:

        get_latest_by = 'created'