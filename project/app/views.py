from django.shortcuts import render
from .models import Fitness

# Create your views here.
def landing(request):
    return render(request,'landing.html')
def regis(request):
        return render(request,'registration.html')
def login(request):
    return render(request,'login.html')
def about(request):
    return render(request,'about.html')

def registion(request):
    username=request.POST.get('fullname')
    email=request.POST.get('email')
    detail=request.POST.get('message')
    phone=request.POST.get('phone')
    age=request.POST.get('age')
    # subscribe=request.POST.getlist('subscribe')
    gender=request.POST.get('gender')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
    plan=request.POST.get('plan')
    # resume=request.FILES.get('resume')
    # print(username,email,detail,phone,dob,subscribe,gender,password,cpassword,profile,resume)

    u=Fitness.objects.filter(Student_email=email)
    if u:
        msg='Email already exist'
        return render(request,'registration.html',{'key':msg})
    else:
        if password==cpassword:
            Fitness.objects.create(Student_name=username,Student_email=email,Student_contact=phone,Student_message=detail,Student_age=age,Student_plan=plan,Student_Gender=gender,Student_Password=password )
            msg='gegistration done'
            return render(request,'login.html',{'keyy':msg})
        else:
            msg1='pssword and cpssword not match'
            return render(request,'registration.html',{'key':msg1})
        
def logindata(request):
    if request.method=='POST':
        email=request.POST.get('email')
        passw=request.POST.get('password')
        user=Fitness.objects.filter(Student_email=email)
        if user:
            userdata=Fitness.objects.get(Student_email=email)
            print(userdata.Student_name)
            print(userdata.Student_email)
            pass1=userdata.Student_Password
            if passw==pass1:
                msg='welcom to dashbord'
                userdata = {
                    "id":userdata.id,
                    "name":userdata.Student_name,
                    "contact":userdata.Student_contact,
                    "dis":userdata.Student_message,
                    "age":userdata.Student_age,
                    "email":userdata.Student_email,
                    # "image":userdata.Student_Image,
                    # "file":userdata.Student_Resume,
                    "plan":userdata.Student_plan,
                    "password":userdata.Student_Password,
                }
                return render(request,'landing.html',{'userdata':userdata})
            else:
                msg='email & password not match'
                return render(request,'login.html',{'msg':msg,'email':email})
        else:
            msg='email not registard'
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
    

        

