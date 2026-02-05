from django.shortcuts import render , redirect
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
        return redirect('view_student')
 return render(request,'student.html')

def view_student(request):
   stu_obj=Student.objects.all()
   return render(request, 'view_student.html',{'students':stu_obj})

def update_student(request,id):
   stu_obj=Student.objects.get(id=id) #fetching the student object based on the provided id
   if request.method=='POST':
       stu_obj.name=request.POST.get('sname')
       stu_obj.usn=request.POST.get('usn')
       stu_obj.email=request.POST.get('email')
       stu_obj.phone=request.POST.get('mob')
       stu_obj.college=request.POST.get('college')
       stu_obj.degree=request.POST.get('degree')
       stu_obj.branch=request.POST.get('branch')
       stu_obj.sem=request.POST.get('sem')
       return redirect('view_students')
   return render(request,'update_student.html',{'student':stu_obj})

def delete_student(request,id):
   stu_obj=Student.objects.get(id=id)
   stu_obj.delete()
   return redirect('view_student')