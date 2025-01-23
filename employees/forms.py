
# employees/forms.py
from django import forms
from .models import Employee, LeaveRequest, Payroll

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['employee', 'start_date', 'end_date', 'reason']

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['employee', 'bonus', 'deductions']
