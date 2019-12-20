from django.db import models


class CommentBox(models.Model):

    emailAddress = models.EmailField()