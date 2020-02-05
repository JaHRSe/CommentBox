from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import UserPassesTestMixin
from commentbox.models import CommentBox, NotificationList, CbType
from .services import  getCommentBoxEmail, getNotifyList,processAdminSave
from .forms import CommentResponseForm
import json

def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser
        return WrappedClass
    return wrapper

def index(request):
    return render(request, "dashboard.html")

@superuser_required()
class DashboardView(View):

    template = "dashboard.html"
    type = None

    def get(self, request, *args, **kwargs):

        ctx = {
            "commentBoxEmail": getCommentBoxEmail(self.type),
            "notifyList": getNotifyList(self.type),
            "commenttype": '224 SS',
        }

        return render(request,
                      context=ctx,
                      template_name=self.template)

    def post(self, request, *args, **kwargs):

        data = json.loads(request.body);
        data['cbType'] = self.type

        if processAdminSave(data):
            status = {"result": True}
        else:
            status = {"result": False}

        return JsonResponse(status)

@superuser_required()
class Save(View):

    def post(self, request, *args, **kwargs):

        if processAdminSave(request.body):
            status = {"result": True}
        else:
            status = {"result": False}

        return JsonResponse(status)


class SSDashboardView(DashboardView):

    template = "ss-dashboard.html"
    type = CbType.SS


class HRADashboardView(DashboardView):
    template = "hra-dashboard.html"
    type = CbType.HRA

@superuser_required()
class CommentResponse(View):

    type = None

    def post(self, request, *args, **kwargs):

        data = json.loads(request.body)

        data['type'] = self.type

        form = CommentResponseForm(data)

        if form.is_valid():
            response = form.save()
            return JsonResponse({})
        else:
            errors = form.errors.as_json()
            return JsonResponse(errors, status=400, safe=False)


class SSCommentResponse(CommentResponse):

    type = CbType.SS.value
