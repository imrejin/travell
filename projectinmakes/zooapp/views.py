from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
      username=request.POST['username']
      password=request.POST['password']
      user=auth.authenticate(username=username,password=password)

      if user is not None:
          auth.login(request,user)
          return redirect('/')
      else:
          messages.info(request,"invalid")
          return  redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method != 'POST':
        return render(request, "register.html")

    username =request.POST['username']
    first_name =request.POST['first_name']
    last_name =request.POST['last_name']
    email =request.POST['email']
    password = request.POST['password']
    confirmpasssword =request.POST['confirm_password']
    if password==confirmpasssword:
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username Taken")
            return redirect('request')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email Taken")
            return redirect('request')
        else:

            user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

        user.save();
        return redirect('/')

    else:
        messages.info(request,"paasword not match")
        return redirect('register')
    return  redirect('/')

    return render(request,"register.html")



def logout(request):
    auth.logout(request)
    return redirect('/')
