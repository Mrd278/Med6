# Generated by Django 2.1.7 on 2019-03-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medchat', '0002_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='id',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]