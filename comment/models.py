from django.db import models
from commentbox.models import CommentBox, CbType
from commentbox.settings.storage_backends import UploadStorage
import uuid


class Comment(models.Model):

    type = models.CharField(max_length=50, choices=CbType.choices(), blank=True, default='')

    box = models.ManyToManyField(CommentBox)

    comment = models.TextField(blank=True)

    created = models.DateField(auto_now_add=True)


class Upload(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    name = models.TextField(max_length=100)

    file = models.FileField(storage=UploadStorage())

    comment = models.ForeignKey(Comment, on_delete=models.PROTECT, null=True)

    created = models.DateTimeField(auto_now_add=True)





