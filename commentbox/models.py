from django.db import models
from django.contrib.postgres.fields import JSONField


class CommentBox(models.Model):

    default='EADSCommentBox@gmail.com'

    emailAddress = models.EmailField(blank=False, default = default)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:

        get_latest_by = 'created'


class NotificationList(models.Model):

    notificationList = JSONField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:

        get_latest_by = 'created'