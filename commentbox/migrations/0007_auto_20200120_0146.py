# Generated by Django 3.0 on 2020-01-20 01:46

import commentbox.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentbox', '0006_auto_20200120_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentbox',
            name='type',
            field=models.CharField(choices=[(commentbox.models.CbType['SS'], 'SS'), (commentbox.models.CbType['HRA'], 'HRA')], default='', max_length=50, null=True),
        ),
    ]
