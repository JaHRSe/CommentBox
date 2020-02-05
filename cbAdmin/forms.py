from django import forms
from .models import CommentResponse
from commentbox.models import CommentBox, NotificationList, CbType


class CommentBoxForm(forms.ModelForm):

    class Meta:
        model = CommentBox
        fields = ('emailAddress', 'type')
        widgets = {
            "emailAddress": forms.TextInput(attrs={'id': 'commentBoxInput'}),
        }


class NotificationListForm(forms.ModelForm):

    class Meta:
        model = NotificationList
        fields = ('notificationList', 'type')


class CommentResponseForm(forms.ModelForm):

    class Meta:
        model = CommentResponse
        fields = {'title', 'body', 'type'}