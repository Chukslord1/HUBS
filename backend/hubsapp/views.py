from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import UserProfile

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']
        cat = request.POST['cat']

        user = auth.authenticate(username=username, password=password, cat=cat)
        if (user is not None) and (cat=="Student"):
            auth.login(request, user)
            return redirect("dashboard2.html")
        elif (user is not None) and (cat=="Teacher"):
            auth.login(request, user)
            return redirect("dashboard4.html")
        elif (user is not None) and (cat=="Parent"):
            auth.login(request, user)
            return redirect("dashboard5.html")
        else:
            return render(request, 'login.html', {"message": "The user does not exist"})
    else:
        return render(request, 'login.html')
def signup(request):
        if request.method == 'POST':
            cat= request.POST['cat']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['pass']
            password2 = request.POST['pass2']
            UserProfile_id=email

            if password1==password2:
                if User.objects.filter(email=email).exists():
                     return render(request, 'sign_up.html', {"message": "The user is already registered"})
                else:
                    user = User.objects.create(username=email, password=password1, email=email )
                    user.set_password(user.password)
                    user.save()
                    profile = UserProfile.objects.create(user=user, cat=cat)
                    profile.save()
            else:
                return render(request, 'sign_up.html', {"message": "The passwords don't match"})
            return redirect('login.html')
        else:
            return render(request, 'sign_up.html')

def dashboard(request):
    return render(request, "dashboard2.html")
def dashboard4(request):
    return render(request, "dashboard4.html")
def dashboard5(request):
    return render(request, "dashboard5.html")
