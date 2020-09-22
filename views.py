from django.shortcuts import render
from django.http import HttpResponse
from .models import Register
from .forms import RegisterForm,LoginForm

# Create your views here.

def regis(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('registration successful')
        else:
            print(form.errors)
            return HttpResponse("error")
    else:
        form = RegisterForm()
        return render(request, 'register.html',{'form': form})
def login(request):
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            un = MyLoginForm.cleaned_data['user_name']
            pw = MyLoginForm.cleaned_data['password']
            dbuser = Register.objects.filter(user_name=un,password=pw)
            if not dbuser:
                return HttpResponse('please check your username and password')
            else:
                return render(request,'success.html')
    else:
        form = LoginForm()
        return render(request, 'loginpage.html',{'form': form})   