from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):

    # ...
    # stu=Student.objects.all() #query set

    # stu = Student.objects.filter(name="Shyam")
    # stu = Student.objects.filter(name="shyam")
    # stu = Student.objects.filter(age=60)

    stu = Student.objects.filter(name="sujan")
    stu=Student.objects.exclude(name="sujan")
    stu=Student.objects.order_by('name')
    stu=Student.objects.order_by('-age')
    stu=Student.objects.order_by('age').reverse()
    stu=Student.objects.order_by('?')
    stu=Student.objects.values('name','age') [:2]
    stu=Student.objects.values('name','age')

    

    return render(request, 'home.html', {'stu':stu})
