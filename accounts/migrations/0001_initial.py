# Generated by Django 2.1.7 on 2019-03-11 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departments', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='doctor_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50, null=True)),
                ('fees', models.CharField(max_length=10, null=True)),
                ('doc_email_id', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100)),
                ('hospital_address', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(blank=True, default='', max_length=30)),
                ('ph_no', models.CharField(blank=True, default='', max_length=10)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=1)),
                ('age', models.IntegerField(blank=True, default='')),
                ('patient_address', models.CharField(blank=True, default='', max_length=200)),
                ('pat_email_id', models.CharField(blank=True, default='', max_length=20)),
                ('doctor', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='accounts.doctor_info')),
            ],
        ),
        migrations.CreateModel(
            name='time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_available', models.DateTimeField(null=True)),
                ('is_available', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='doctor_info',
            name='Availabilty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.time'),
        ),
        migrations.AddField(
            model_name='doctor_info',
            name='Hospital_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Hospital', to='accounts.hospital'),
        ),
        migrations.AddField(
            model_name='doctor_info',
            name='dpt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='accounts.Department'),
        ),
    ]
