from django.db import models
from commentbox.models import CommentBox

class Comment(models.Model):

    box = models.ManyToManyField(CommentBox)

    comment = models.TextField()

    created = models.DateField(auto_now_add=True)




