from django import forms
from django.core.validators import validate_email


from .models import EmployeeProfile

class AddEmployeeForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    employee_code = forms.CharField(max_length=15, required=True)
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

    class Meta:
        model = EmployeeProfile
