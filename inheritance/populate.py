import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','inheritance.settings')
import django
django.setup()

from testapp.models import  Employee1
from random import choice,randint

def populate(n):
    for i in range(n):
        eno=randint(1001,9999)
        ename=choice(["A","B","C","D"])  + str(randint(1,99999))
        esal=randint(10000,99999)
        eaddr=choice(["A","B","C","D"])  + str(randint(1,99999))
        print(eno,ename,esal,eaddr)
        emp_record=Employee1.objects.get_or_create(eno=eno,ename=ename,esal=esal,eaddr=eaddr)
populate(20)


       