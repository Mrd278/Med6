# Generated by Django 2.1.7 on 2019-03-08 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=30)),
                ('Hospital_address', models.CharField(max_length=100)),
                ('date_application', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
