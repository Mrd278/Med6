# Generated by Django 2.1.7 on 2019-03-08 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medchat', '0004_auto_20190308_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='medchat.Doctor'),
        ),
    ]
