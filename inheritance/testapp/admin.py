
# Register your models here.
from django.contrib import admin
# Register your models here.
'''
from testapp.models import Teacher1,Student1,ContactInfo
class ContactInfoAdmin(admin.ModelAdmin):
    list_display=['name','email','address']
class Student1Admin(admin.ModelAdmin):
    list_display=['name','email','address','marks','rollno']
class Teacher1Admin(admin.ModelAdmin):
    list_display=['name','email','address','marks','rollno']
admin.site.register(Student1,Student1Admin)
admin.site.register(Teacher1,Teacher1Admin)
admin.site.register(ContactInfo,ContactInfoAdmin)
'''

'''
#Multiple inheritance
from testapp.models import Parent1,Parent2,Child
class Parent1Admin(admin.ModelAdmin):
    list_display=['f1','f2']
class Parent2Admin(admin.ModelAdmin):
    list_display=['f3','f4']
class ChildAdmin(admin.ModelAdmin):
    list_display=['f5','f6']
admin.site.register(Parent1,Parent1Admin)
admin.site.register(Parent2,Parent2Admin)
admin.site.register(Child,ChildAdmin)
'''

'''
#MultiLevel inheritance
from testapp.models import Employee,Person,Manager

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','age','eno','esal']

class PersonAdmin(admin.ModelAdmin):
    list_display=['age','name']

class ManagerAdmin(admin.ModelAdmin):
    list_display=['name','age','eno','esal','exp','team_size']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(Manager,ManagerAdmin)
'''



# DEMO APPLICATION
from testapp.models import Employee1,ProxyEmployee2,ProxyEmployee3

class Employee1Admin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

class ProxyEmployee2Admin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

class ProxyEmployee3Admin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

admin.site.register(Employee1,Employee1Admin)
admin.site.register(ProxyEmployee2,ProxyEmployee2Admin)
admin.site.register(ProxyEmployee3,ProxyEmployee3Admin)
