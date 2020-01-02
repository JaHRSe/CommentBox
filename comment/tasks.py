from .services import emailComment
from celery import shared_task
from .models import Comment

@shared_task()
def email(commentId):
    comment = Comment.objects.get(pk=commentId)
    emailComment(comment)