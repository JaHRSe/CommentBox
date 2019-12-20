from django.shortcuts import render
from django.views import View
from .forms import CommentBoxForm
from commentbox.models import CommentBox


class DashboardView(View):

    template = "dashboard.html"

    def get(self, request, *args, **kwargs):

        ctx = {
            "commentBoxForm": CommentBoxForm(instance=CommentBox.objects.last()),
        }

        return render(request,
                      context=ctx,
                      template_name=self.template)

# Create your views here.
