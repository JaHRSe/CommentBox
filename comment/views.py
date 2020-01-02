from django.views import View
from django.shortcuts import render, redirect
from .forms import CommentForm, UploadForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .models import Upload
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from .services import emailComment
from .tasks import email

class Comment(View):

    form = CommentForm

    template = "comment.html"

    def get(self, request, *args, **kwargs):

        # Make sure user is logged in
        if not request.user.is_authenticated:
            return redirect('anonLogin')

        ctx = {'form':self.form()}

        return render(request,
                      template_name=self.template,
                      context=ctx)

    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('anonLogin')

        data = json.loads(request.body)

        # Save the comment
        form = self.form(data)

        comment = None

        if form.is_valid():
            comment = form.save()
        else:
            pass
        #return error

        # cycle through file IDs and associate with comment
        for file in data['files']:
            file = json.loads(file)
            obj = Upload.objects.get(pk=file['id'])
            obj.comment = comment
            obj.save()

        # Send out email notification
        emailComment(comment)
        # email.delay(comment.id)

        return redirect('comment:comment')


@method_decorator(csrf_exempt, name='dispatch')
class UploadView(LoginRequiredMixin, View):

    form = UploadForm

    def post(self,request, *args, **kwargs):


        post = {'file':{}, 'name':request.FILES['filepond'].name}
        file = {'file':request.FILES['filepond']}

        form = self.form(post, file)

        if form.is_valid():
            file = form.save()
            return JsonResponse({'id': file.id})
        else:
            return JsonResponse({})