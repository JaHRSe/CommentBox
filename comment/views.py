from django.views import View
from django.shortcuts import render, redirect
from .forms import CommentForm


class Comment(View):

    form = CommentForm

    template = "comment.html"

    def get(self, request, *args, **kwargs):

        ctx = {'form':self.form()}

        return render(request,
                      template_name=self.template,
                      context=ctx)

    def post(self, request, *args, **kwargs):

        form = self.form(request.POST)

        if form.is_valid():

            form = form.save()

        else:
            pass

        return redirect('comment:comment')