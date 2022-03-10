from django.conf.urls import url
from applications.employee import views
app_name = 'employee'


urlpatterns = [
    url(r'^$', (views.HomePageView.as_view()), name='home'),
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^add-employee/$', views.AddEmployeeView.as_view(), name="add-employee"),
    url(r'^view-employees/$', views.EmployeeView.as_view(), name="view-employees"),
    url(r'^employee-details/(?P<id>\d+)$', views.EmployeeDetailsView.as_view(), name="employee-details"),
    url(r'^delete-employee/(?P<id>\d+)$', views.DeleteEmployeeView.as_view(), name="delete-employee"),
    url(r'^edit-employee/(?P<id>\d+)$', views.EditEmployeeView.as_view(), name="edit-employee"),
    url(r'^add-student/$', views.AddStudentView.as_view(), name="add-student"),
    url(r'^add-marks/$', views.AddMarksView.as_view(), name="add-marks"),
  ]