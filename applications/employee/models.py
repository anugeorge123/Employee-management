from django.db import models

class UserProfle(models.Model):
    gmail_id = models.CharField(max_length=30,null=True, blank=True)

    def __str__(self):
        return str(self.gmail_id)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

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

class StudentProfile(models.Model):
    name = models.CharField(max_length=30,null=True, blank=True)
    regitration_no = models.CharField(max_length=30,null=True, blank=True)
    department = models.CharField(max_length=30,null=True, blank=True)
    academic_year = models.CharField(max_length=30,null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Student Profile"
        verbose_name_plural = "Student Profiles"

class Subject(models.Model):
    subject_name = models.CharField(max_length=30,null=True, blank=True)

    def __str__(self):
        return str(self.subject_name)


class StudentMark(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.CharField(max_length=10,null=True, blank=True)