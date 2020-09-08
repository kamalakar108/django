from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from testapp.models import Employee,ProxyEmployee,ProxyEmployee2
# Create your views here.
def display_view(request):
# employees=Employee.objects.all()
# employees=ProxyEmployee.objects.all()
    employees=ProxyEmployee2.objects.all()
    my_dict={'employees':employees}
    return render(request,'testapp/index.html',my_dict)
