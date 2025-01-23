# # employees/views.py
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Employee, LeaveRequest
# from .forms import EmployeeForm, LeaveRequestForm

# # Employee views
# def employee_list(request):
#     employees = Employee.objects.all()
#     return render(request, "employee_list.html", {"employees": employees})

# def employee_create(request):
#     form = EmployeeForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("employee_list")
#     return render(request, "employee_form.html", {"form": form})

# def employee_update(request, pk):
#     employee = get_object_or_404(Employee, pk=pk)
#     form = EmployeeForm(request.POST or None, instance=employee)
#     if form.is_valid():
#         form.save()
#         return redirect("employee_list")
#     return render(request, "employee_form.html", {"form": form})

# def employee_delete(request, pk):
#     employee = get_object_or_404(Employee, pk=pk)
#     employee.delete()
#     return redirect("employee_list")

# # Leave requests views
# def leave_requests(request):
#     leave_requests = LeaveRequest.objects.all()
#     return render(request, "leave_requests.html", {"leave_requests": leave_requests})

# def leave_approve(request, pk):
#     leave_request = get_object_or_404(LeaveRequest, pk=pk)
#     leave_request.status = "Approved"
#     leave_request.save()
#     return redirect("leave_requests")

# def leave_reject(request, pk):
#     leave_request = get_object_or_404(LeaveRequest, pk=pk)
#     leave_request.status = "Rejected"
#     leave_request.save()
#     return redirect("leave_requests")

# # Add new leave request view
# def leave_request_create(request):
#     if request.method == 'POST':
#         form = LeaveRequestForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the leave request
#             return redirect('leave_requests')  # Redirect to the leave requests page
#     else:
#         form = LeaveRequestForm()

#     return render(request, 'add_leave_request.html', {'form': form})








# employees/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, LeaveRequest, Payroll
from .forms import EmployeeForm, LeaveRequestForm, PayrollForm

# Employee views
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employee_list.html", {"employees": employees})

def employee_create(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request, "employee_form.html", {"form": form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("employee_list")
    return render(request, "employee_form.html", {"form": form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect("employee_list")

# Leave requests views
def leave_requests(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, "leave_requests.html", {"leave_requests": leave_requests})

def leave_approve(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    leave_request.status = "Approved"
    leave_request.save()
    return redirect("leave_requests")

def leave_reject(request, pk):
    leave_request = get_object_or_404(LeaveRequest, pk=pk)
    leave_request.status = "Rejected"
    leave_request.save()
    return redirect("leave_requests")

def leave_request_create(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_requests')
    else:
        form = LeaveRequestForm()
    return render(request, 'add_leave_request.html', {'form': form})

# Payroll views
def payroll_list(request):
    payrolls = Payroll.objects.all()
    return render(request, "payroll_list.html", {"payrolls": payrolls})

def payroll_create(request):
    form = PayrollForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("payroll_list")
    return render(request, "payroll_form.html", {"form": form})

def payroll_update(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    form = PayrollForm(request.POST or None, instance=payroll)
    if form.is_valid():
        form.save()
        return redirect("payroll_list")
    return render(request, "payroll_form.html", {"form": form})

def payroll_delete(request, pk):
    payroll = get_object_or_404(Payroll, pk=pk)
    payroll.delete()
    return redirect("payroll_list")
