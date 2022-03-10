from django import forms
from django.core.validators import validate_email


from .models import EmployeeProfile,StudentProfile,StudentMark

class AddEmployeeForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    # employee_code = forms.CharField(max_length=15, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    email = forms.CharField(widget=forms.EmailInput(), required=True)
    address = forms.CharField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except:
            raise forms.ValidationError('Invalid email')
        return email

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data['phone_number']
    #     if not phone_number.is_decimal():
    #         raise forms.ValidationError('Phone number must be numeric value!')
    #     return phone_number

    class Meta:
        model = EmployeeProfile


class AddStudentForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    registration_no = forms.CharField(max_length=15, required=True)
    department = forms.CharField(max_length=30,  required=True)
    academic_year = forms.CharField(max_length=15, required=True)

    class Meta:
        model = StudentProfile

class AddMarkForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    registration_no = forms.CharField(max_length=15, required=True)
    subject = forms.CharField(max_length=30,  required=True)
    mark = forms.CharField(max_length=15, required=True)

    class Meta:
        model = StudentMark

class LoginForm(forms.Form):
    gmail_id = forms.CharField(widget=forms.EmailInput(), required=True)

    def clean_gmail_id(self):
        gmail_id = self.cleaned_data['gmail_id']
        try:
            validate_email(gmail_id)
        except:
            raise forms.ValidationError('Invalid gmail id')
        return gmail_id