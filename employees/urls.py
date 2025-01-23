
# employees/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.employee_list, name="employee_list"),
    path("create/", views.employee_create, name="employee_create"),
    path("<int:pk>/edit/", views.employee_update, name="employee_update"),
    path("<int:pk>/delete/", views.employee_delete, name="employee_delete"),
    path("leave_requests/", views.leave_requests, name="leave_requests"),
    path("leave_requests/<int:pk>/approve/", views.leave_approve, name="leave_approve"),
    path("leave_requests/<int:pk>/reject/", views.leave_reject, name="leave_reject"),
    path("leave_requests/create/", views.leave_request_create, name="leave_request_create"),
    path("payroll/", views.payroll_list, name="payroll_list"),
    path("payroll/create/", views.payroll_create, name="payroll_create"),
    path("payroll/<int:pk>/edit/", views.payroll_update, name="payroll_update"),
    path("payroll/<int:pk>/delete/", views.payroll_delete, name="payroll_delete"),
]
