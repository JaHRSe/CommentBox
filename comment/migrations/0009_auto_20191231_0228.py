# Generated by Django 3.0 on 2019-12-31 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0008_auto_20191231_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]