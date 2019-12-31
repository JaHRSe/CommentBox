from django.db import models
from commentbox.models import CommentBox
import uuid

class Comment(models.Model):

    box = models.ManyToManyField(CommentBox)

    comment = models.TextField(blank=True)

    created = models.DateField(auto_now_add=True)


class Upload(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    name = models.TextField(max_length=100)

    file = models.FileField(upload_to='uploads/')

    comment = models.ForeignKey(Comment, on_delete=models.PROTECT, null=True)

    created = models.DateTimeField(auto_now_add=True)





