from django.db import models

class EmployeeProfile(models.Model):
    name = models.CharField(max_length=30,null=True, blank=True)
    employee_code = models.CharField(max_length=30,null=True, blank=True)
    phone_number = models.CharField(max_length=30,null=True, blank=True)
    email = models.CharField(max_length=30,null=True, blank=True)
    address = models.CharField(max_length=30,null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Employee Profile"
        verbose_name_plural = "Employee Profiles"
