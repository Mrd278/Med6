from django.db import models

class Doctor(models.Model):
    doctor_name=models.CharField(primary_key=True,max_length=30)
    Hospital_address=models.CharField(max_length=100)
    date_application=models.DateTimeField(auto_now_add=False,null=False)

    def __str__(self):
        return self.doctor_name

class Patient(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='doctor')
    patient_name=models.CharField(max_length=30)

    def __str__(self):
        return self.patient_name