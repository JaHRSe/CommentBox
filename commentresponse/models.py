from django.db import models


class CommentResponse(models.Model):

    type = models.CharField(max_length=50, blank=True, default='')

    title = models.TextField(max_length=120, null=False, blank=False, unique=True)

    body = models.TextField(max_length=10000)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)


    @property
    def wordcount(self):
        return len(self.body.split())
