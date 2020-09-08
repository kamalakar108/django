from django.db import models

# Create your models here.
# Without Inheritance
'''
class Student(models.Model):
 name=models.CharField(max_length=64)
 email=models.EmailField()
 address=models.CharField(max_length=256)
 rollno=models.IntegerField()
 marks=models.IntegerField()

class Teacher(models.Model):
  name=models.CharField(max_length=64)
  email=models.EmailField()
  address=models.CharField(max_length=256)
  subject=models.CharField(max_length=64)
  salary=models.FloatField()
'''
# With Inheritance
'''
class ContactInfo(models.Model):
  name=models.CharField(max_length=64)
  email=models.EmailField()
  address=models.CharField(max_length=256)
  class Meta:
     abstract=True
'''
'''
class Student1(ContactInfo):
   rollno=models.IntegerField()
   marks=models.IntegerField()

class Teacher1(ContactInfo):
  subject=models.CharField(max_length=64)
  salary=models.FloatField()

'''
'''
# Multiple Inheritance:
class Parent1(models.Model):
   f1=models.CharField(max_length=64)
   f2=models.CharField(max_length=64)

class Parent2(models.Model):
  f3=models.CharField(max_length=64)
  f4=models.CharField(max_length=64)

class Child(Parent1,Parent2):
  f5=models.CharField(max_length=64)
  f6=models.CharField(max_length=64)
'''
'''

# Multi Table Inheritance:
class BasicModel(models.Model):
  f1=models.CharField(max_length=64)
  f2=models.CharField(max_length=64)
  f3=models.CharField(max_length=64)

class StandardModel(BasicModel):
  f4=models.CharField(max_length=64)
  f5=models.CharField(max_length=64)

'''
'''
# Multi Level Inheritance:
class Person(models.Model):
  name=models.CharField(max_length=64)
  age=models.IntegerField()

class Employee(Person):
  eno=models.IntegerField()
  esal=models.FloatField()

class Manager(Employee):
  exp=models.IntegerField()
  team_size=models.IntegerField()
'''

#DEMO APPLICATION

class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=15000)

class CustomManager2(models.Manager):
    def get_queryset(self):
            return super().get_queryset().order_by('ename')

class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(eno__lt=1000)

class Employee1(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)
    objects=CustomManager1()

class ProxyEmployee2(Employee1):
    objects=CustomManager2()
    class Meta:
        proxy=True

class ProxyEmployee3(Employee1):
    objects=CustomManager3()
    class Meta:
        proxy=True
