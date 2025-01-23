from django.contrib import admin
from .models import Employee, LeaveRequest

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "position", "salary", "date_hired")

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ("employee", "start_date", "end_date", "reason", "status")
