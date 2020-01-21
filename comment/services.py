from django.core import mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from commentbox.models import NotificationList, CommentBox


def sendMail(emailTxt, attachments, cbType):

    try:
        inbox = CommentBox.objects.filter(type=cbType).latest().emailAddress
    except:
        inbox = ''


    nl=None

    if NotificationList.objects.filter(type=cbType).exists():
        nl = NotificationList.objects.filter(type=cbType).latest().notificationList

    if not nl: nl = []

    nl.append(inbox)

    msg = EmailMessage('Comment submitted',
                       emailTxt,
                       'eadscommentbox@gmail.com',
                       nl)
    for file in attachments:
        msg.attach(file.file.name, file.file.read())

    msg.send()


def emailComment(comment):

    attachments = []

    if comment.upload_set.all().exists():
        attachments = comment.upload_set.all()

    ctx ={
        'date':comment.created,
        'attachmentCount': len(attachments),
        'comment': comment.comment,
    }

    msg_plain= render_to_string('commentEmail', ctx)

    sendMail(msg_plain, attachments, comment.type)



