from django import forms
from commentbox.models import CommentBox, NotificationList


class CommentBoxForm(forms.ModelForm):

    class Meta:
        model = CommentBox
        fields = ('emailAddress', )
        widgets={
            "emailAddress":forms.TextInput(attrs={'id':'commentBoxInput'}),
        }


class NotificationListForm(forms.ModelForm):

    class Meta:
        model=NotificationList
        fields=('notificationList',)
