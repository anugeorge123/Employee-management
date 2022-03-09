import json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


from applications.employee.forms import AddEmployeeForm
from applications.employee.models import EmployeeProfile


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(self.request, 'login.html')

class AddEmployeeView(View):

    def get(self, request, *args, **kwargs):
        return render(self.request, 'add_employee.html')

    def post(self, request, *args, **kwargs):
        data = {}
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            name = self.request.POST['name']
            employee_code = request.POST.get('employee_code', None)
            phone_number = request.POST.get('phone_number',None)
            email = self.request.POST.get('email',None)
            address = request.POST.get('address',None)
            try:
                print("try")
                employee = EmployeeProfile.objects.create(name=name,employee_code=employee_code,
                                                          phone_number=phone_number,email=email,
                                                          address=address)
                data['result'] = "success"

            except:
                data['result'] = "error"

        else:
            data['result'] = "form_error"
            data['error'] = form.errors
        return HttpResponse(json.dumps(data), content_type="application/json")

class EmployeeView(View):

    def get(self, request, *args, **kwargs):
        employee = EmployeeProfile.objects.all()
        print(employee,"============>")
        return render(self.request, 'view_total_employees.html',{'employee':employee})


class EmployeeDetailsView(View):
    def get(self, request, id, *args, **kwargs):
        print("id",id)
        employee = EmployeeProfile.objects.get(id=id)
        print("EMPLOYEE ",employee)
        return render(self.request, 'view_employee.html',{'employee':employee})


    # def post(self, request, id, *args, **kwargs):
    #     data = dict()
    #     print("id", id)
    #     try:
    #         employee = EmployeeProfile.objects.get(id=id)
    #         print("EMPLOYEE ", employee)
    #         print("deleted")
    #         # employee.delete()
    #         data['result'] = "success"
    #     except:
    #         data['result'] = "failed"
    #     # return render(self.request, 'view_total_employees.html',{'employee':employee})
    #     return HttpResponse(json.dumps(data), content_type="application/json")

class DeleteEmployeeView(View):
    def get(self, request, id, *args, **kwargs):
        data = dict()
        try:
            employee = EmployeeProfile.objects.get(id=id)
            employee.delete()
            data['result'] = "success"
        except:
            data['result'] = "failed"
        return HttpResponse(json.dumps(data), content_type="application/json")


class EditEmployeeView(View):
    def post(self, request, id, *args, **kwargs):
        data = dict()
        name = self.request.POST.get('name', None)
        employee_code = self.request.POST.get('employee_code', None)
        phone_number = self.request.POST.get('phone_number', None)
        email = self.request.POST.get('email', None)
        address = self.request.POST.get('address', None)

        try:
            print("id==> ",id)
            employee = EmployeeProfile.objects.get(id=id)
            employee.name = name
            employee.employee_code = employee_code
            employee.phone_number = phone_number
            employee.email = email
            employee.address = address
            data['result'] = "success"
        except:
            data['result'] = "failed"
        return HttpResponse(json.dumps(data), content_type="application/json")

