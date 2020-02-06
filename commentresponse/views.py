from django.shortcuts import render
from django.views.generic.list import ListView
from .models import CommentResponse
from comment.models import CbType


class CommentResponseView(ListView):

    type = None

    context_object_name = 'cr'

    model = CommentResponse

    template_name = 'response-board.html'

    def get_queryset(self):
        return CommentResponse.objects.filter(type=self.type)


class SSCommentResponseView(CommentResponseView):

    type = CbType.SS.value

