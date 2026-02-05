from django.shortcuts import render
from .models import Student

def index(request):
 return render(request, 'index.html')

def student(request):
 if request.method=='POST':
        #reading / fetching register form data
        name=request.POST.get('sname')
        usn=request.POST.get('usn')
        email=request.POST.get('email')
        phone=request.POST.get('mob')
        college=request.POST.get('college')
        degree=request.POST.get('degree')
        branch=request.POST.get('branch')
        sem=request.POST.get('sem')

        
        stu_obj=Student()
        stu_obj.name=name
        stu_obj.usn=usn
        stu_obj.email=email
        stu_obj.phone=phone
        stu_obj.college=college
        stu_obj.degree=degree
        stu_obj.branch=branch
        stu_obj.sem=sem
        stu_obj.save()

        # printing fetched data on console --> to Comform
        # print("Name :",name)
        # print("USN :",usn)
        # print("email :",email)
        # print("phone :",phone)
        # print("college :",college)
        # print("degree :",degree)
        # print("sem :",sem)
 return render(request,'student.html')