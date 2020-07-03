from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    return render(request,'operations/index.html')

def addstudent(request):

        return render(request, 'operations/add.html')




def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        studentid = request.POST['studentid']
        age = request.POST['age']
        section = request.POST['section']
        register = Student(name=name, email=email, studentid=studentid, age=age, section=section)
        register.save()
        return render(request,'operations/add.html')

def view(request):

    seeinfro=Student.objects.all()
    infro={
        'infro':seeinfro
    }
    return render(request,'operations/view.html',infro)

def delete(request, id):

    list = Student.objects.get(pk=id)
    list.delete()
    list1=Student.objects.all()
    return render(request, 'operations/view.html',{'infro':list1})

def edit(request,id):
    value=Student.objects.get(pk=id)
    context={
        'value':value
    }

    return render(request,'operations/edit.html',context)

def update(request,id=None):
    if request.method=="POST":
        if id is not None:
            value=Student.objects.get(id=id)



            value.name = request.POST['name']
            value.email = request.POST['email']
            value.studentid = request.POST['studentid']
            value.age = request.POST['age']
            value.section = request.POST['section']
            value.save()

    return redirect(view)


def search(request):
    givenname=request.POST['name']
    student=Student.objects.filter(name__iexact=givenname)
    return render(request,'operations/view.html',{'infro':student})



