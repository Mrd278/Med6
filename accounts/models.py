from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class time(models.Model):
    time_available=models.DateTimeField(null=True)
    is_available=models.BooleanField(default=False)

    def __str__(self):
        return '%s' %self.time_available

class hospital(models.Model):
    hospital_name=models.CharField(max_length=100)
    hospital_address=models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.hospital_name

class Department(models.Model):
    departments=models.CharField(max_length=30)

    def __str__(self):
        return self.departments

class doctor_info(models.Model):
    doctor_name=models.CharField(max_length=50,null=True)
    Availabilty=models.ForeignKey(time,on_delete=models.CASCADE)
    dpt=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department',null=True)
    Hospital_info=models.OneToOneField(hospital,on_delete=models.CASCADE,related_name='Hospital',null=True)
    fees=models.CharField(max_length=10,null=True)
    doc_email_id=models.CharField(max_length=40)

    def __str__(self):
        return self.doctor_name

class patient(models.Model):
    doctor=models.ForeignKey(doctor_info,on_delete=models.CASCADE,related_name='doctor',blank=True,default='')
    patient_name=models.CharField(max_length=30,blank=True,default='')
    ph_no=models.CharField(max_length=10,blank=True,default='')
    gender_choices=models.gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(choices=gender_choices,max_length=1,default='',blank=True)
    age=models.CharField(max_length=3,blank=True,default='')
    patient_address=models.CharField(max_length=200,default='',blank=True)
    pat_email_id=models.CharField(max_length=20,blank=True,default='')

    def __str__(self):
        return self.patient_name
