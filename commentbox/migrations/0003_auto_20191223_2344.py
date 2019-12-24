# Generated by Django 3.0 on 2019-12-23 23:44

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentbox', '0002_notificationlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationlist',
            name='notificationList',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='commentbox',
            name='emailAddress',
            field=models.EmailField(default='EADSCommentBox@gmail.com', max_length=254),
        ),
    ]
