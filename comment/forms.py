from django import forms
from .models import Comment, Upload


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment', 'type']


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['name', 'file']





