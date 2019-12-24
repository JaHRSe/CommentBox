from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from .services import  getCommentBoxEmail, getNotifyList,processAdminSave

def superuser_required():
    def wrapper(wrapped):
        class WrappedClass(UserPassesTestMixin, wrapped):
            def test_func(self):
                return self.request.user.is_superuser
        return WrappedClass
    return wrapper

@superuser_required()
class DashboardView(View):

    template = "dashboard.html"

    def get(self, request, *args, **kwargs):

        ctx = {
            "commentBoxEmail": getCommentBoxEmail(),
            "notifyList": getNotifyList(),
        }

        return render(request,
                      context=ctx,
                      template_name=self.template)

@superuser_required()
class Save(View):

    def post(self, request, *args, **kwargs):

        if processAdminSave(request.body):
            status = {"result": True}
        else:
            status = {"result": False}

        return JsonResponse(status)


# Create your views here.
