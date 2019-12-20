from django import forms
from commentbox.models import CommentBox


class CommentBoxForm(forms.ModelForm):

    class Meta:
        model = CommentBox
        fields = ('emailAddress', )
