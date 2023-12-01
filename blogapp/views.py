from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.views import View

class MaqolalarView(View):
    def get(self,request):
        content={
            "maqolalar": Maqola.objects.all()
        }
        return render(request, 'home.html', content)


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/login/')

class LoginView(View):

    def post(self,request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('/')
        return redirect('/login/')

    def get(self,request):
        return render(request,'login.html')

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        User.objects.create_user(
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            password=request.POST.get("password")
        )

        return redirect('/home/')

class MaqolaView(View):
    def get(self,request,son):
        content={
            "maqola": Maqola.objects.get(id=son),
        }
        return render(request, 'maqola.html', content)

class Yangimaqola(View):
     def get(self,request):
         return render(request,'yangi.html')