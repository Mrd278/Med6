from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(patient)
admin.site.register(doctor_info)
admin.site.register(time)
admin.site.register(hospital)
admin.site.register(Department)

