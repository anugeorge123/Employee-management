from django.contrib import admin
from .models import EmployeeProfile,StudentProfile,Subject,StudentMark

admin.site.register(EmployeeProfile, admin.ModelAdmin)
admin.site.register(StudentProfile, admin.ModelAdmin)
admin.site.register(Subject, admin.ModelAdmin)
admin.site.register(StudentMark, admin.ModelAdmin)
