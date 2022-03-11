import json

from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse


from applications.employee.forms import AddEmployeeForm,AddStudentForm,AddMarkForm,LoginForm
from applications.employee.models import EmployeeProfile,StudentProfile,Subject,StudentMark,UserProfle

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(self.request, 'index.html')


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(self.request, 'login.html')

    def post(self, request, *args, **kwargs):
        data = {}
        form = LoginForm(request.POST)
        if form.is_valid():
            gmail_id = self.request.POST['gmail_id']
            try:
                log = UserProfle.objects.create(gmail_id=gmail_id)
                if log:
                    data['result'] = "success"
                    return redirect('employee:add-employee')
                else:
                    data['result'] = "error"
            except:
                data['result'] = "error"
        else:
            data['result'] = "form_error"
            data['error'] = form.errors
            print("form error: ",form.errors)
        return HttpResponse(json.dumps(data), content_type="application/json")


class AddEmployeeView(View):

    def get(self, request, *args, **kwargs):
        return render(self.request, 'add_employee.html')

    def post(self, request, *args, **kwargs):
        data = {}
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            name = self.request.POST['name']
            # employee_code = request.POST.get('employee_code', None)
            phone_number = request.POST.get('phone_number',None)
            email = self.request.POST.get('email',None)
            address = request.POST.get('address',None)
            try:
                employee = EmployeeProfile.objects.create(name=name,phone_number=phone_number,email=email,
                                                          address=address)
                data['result'] = "success"

            except:
                data['result'] = "error"
        else:
            data['result'] = "form_error"
            data['error'] = form.errors
            print("form error: ",form.errors)
        return HttpResponse(json.dumps(data), content_type="application/json")

class EmployeeView(View):

    def get(self, request, *args, **kwargs):
        employee = EmployeeProfile.objects.all()
        return render(self.request, 'view_total_employees.html',{'employee':employee})


class EmployeeDetailsView(View):
    def get(self, request, id, *args, **kwargs):
        employee = EmployeeProfile.objects.get(id=id)
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
        data = {}
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            name = self.request.POST.get('name', None)
            employee_code = self.request.POST.get('employee_code', None)
            phone_number = self.request.POST.get('phone_number', None)
            email = self.request.POST.get('email', None)
            address = self.request.POST.get('address', None)

            try:
                employee = EmployeeProfile.objects.get(id=id)
                employee.name = name
                employee.employee_code = employee_code
                employee.phone_number = phone_number
                employee.email = email
                employee.address = address
                data['result'] = "success"
            except:
                data['result'] = "failed"

        else:
            data['result'] = "form_error"
            data['error'] = form.errors
            print("form error: ", form.errors)
        return HttpResponse(json.dumps(data), content_type="application/json")


class AddStudentView(View):

    def get(self, request, *args, **kwargs):
        return render(self.request, 'add_student.html')

    def post(self, request, *args, **kwargs):
        data = {}
        form = AddStudentForm(request.POST)
        if form.is_valid():
            name = self.request.POST['name']
            registration_no = request.POST.get('registration_no',None)
            department = self.request.POST.get('department',None)
            academic_year = request.POST.get('academic_year',None)
            try:
                print("try")
                student = StudentProfile.objects.create(name=name,regitration_no=registration_no,department=department,
                                                          academic_year=academic_year)
                if student:
                    data['result'] = "success"
                else:
                    data['result'] = "Internal Server Error"

            except:
                data['result'] = "error"
        else:
            data['result'] = "form_error"
            data['error'] = form.errors
            print("form error: ",form.errors)
        return HttpResponse(json.dumps(data), content_type="application/json")


class AddMarksView(View):

    def get(self, request,  *args, **kwargs):
        name = request.GET.get('name', None)
        registration_no = request.GET.get('registration_no', None)
        subject = Subject.objects.all()
        return render(self.request, 'add_marks.html',{'name':name,'registration_no':registration_no,
                                                      'subject':subject})

    def post(self, request, *args, **kwargs):
        data = {}
        form = AddMarkForm(request.POST)
        if form.is_valid():
            name = self.request.POST['name']
            registration_no = request.POST.get('registration_no', None)
            subject = self.request.POST.get('subject', None)
            mark = request.POST.get('mark', None)
            stu = StudentProfile.objects.get(regitration_no=registration_no)
            print("stu",stu)
            try:
                print("try")
                # mark = StudentMark.objects.create(student=stu,subject_name=subject,
                #                                      mark=mark)
                mark = StudentMark()
                mark.student = stu.name
                mark.subject_name = subject
                mark.mark = mark
                mark.save()
                if mark:
                    print("iff")
                    data['result'] = "success"
                else:
                    print("else")
                    data['result'] = "Internal Server Error"
            except Exception as e:
                print("except")
                data['result'] = "error"
        else:
            data['result'] = "form_error"
            data['error'] = form.errors
            print("form error: ", form.errors)
        return HttpResponse(json.dumps(data), content_type="application/json")
