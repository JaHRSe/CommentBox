from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .services import getNotifyList

from .forms import CommentBoxForm
from commentbox.models import CommentBox
from .services import processAdminSave


class DashboardView(View):

    template = "dashboard.html"

    def get(self, request, *args, **kwargs):

        ctx = {
            "commentBoxForm": CommentBoxForm(instance=CommentBox.objects.last()),
            "notifyList" : getNotifyList(),
        }

        return render(request,
                      context=ctx,
                      template_name=self.template)


class Save(View):

    def post(self, request, *args, **kwargs):

        if processAdminSave(request.body):
            status = {"result": True}
        else:
            status = {"result": False}

        return JsonResponse(status)


# Create your views here.
