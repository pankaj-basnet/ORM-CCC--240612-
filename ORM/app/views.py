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

    stu=Student.objects.get(id=6)
    stu=Student.objects.first()
    stu=Student.objects.last()
    stu=Student.objects.latest("age")
    stu=Student.objects.earliest('name')

    # latest= highest in age biggest --- sujan before pankaj if in name latest
    # earlier= lowest in age biggest --- sujan after pankaj if in name earlier

    # stu=Student.objects.create(name="ram add", age=25, email="sujan@gmail.com", address="pkr")
    # stu=Student.objects.filter(id=1).update(name="sujan update")

    ### lookups
    ## to use loop ----lookup used-----useful in frontend
    # iexact=== removes case-sensitive---lower or uppercase--doesnot matter
    stu=Student.objects.filter(name__exact="sujan")
    stu=Student.objects.filter(name__iexact="sujan")
    stu=Student.objects.filter(name__icontains="an")
    stu=Student.objects.filter(name__startswith="suj")
    stu=Student.objects.filter(name__endswith="an")
    stu=Student.objects.filter(age__gt=20)
    stu=Student.objects.filter(age__gte=20)
    stu=Student.objects.filter(age__lte=20)
    stu=Student.objects.filter(age__range=(20,40))

    

    return render(request, 'home.html', {'i':stu})
    return render(request, 'home.html', {'stu':stu})
