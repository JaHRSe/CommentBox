# Generated by Django 3.0 on 2020-01-20 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentbox', '0008_auto_20200120_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentbox',
            name='type',
            field=models.CharField(blank=True, choices=[('SS', 'SS'), ('HRA', 'HRA'), ('TEST', 'TS')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='notificationlist',
            name='type',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
