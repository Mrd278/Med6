# Generated by Django 2.1.7 on 2019-03-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medchat', '0003_auto_20190308_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='date_application',
            field=models.DateTimeField(),
        ),
    ]
