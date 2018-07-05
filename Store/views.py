from django.shortcuts import render
from .forms import loginForm

#login
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
# Create your views here.
from Store.forms  import UserForm,UserProfileInfoForm
def login_page(request):
    if request.method == 'POST':
     form = loginForm(request.POST or None)
     print('ssssshhhhhhhhhhhhhh')
     if form.is_valid():
         print("hhhhh")
    else:
        form = loginForm()
    return render(request,"auth/login_two_columns.html",{'form':form} )
def register(request):
    registreed = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)#hashin password
            user.save()

            profile = profile_form.save(commit= False )
            profile.user = user #onetoone

            if 'picture' in request.FILES :
                profile.picture = request.FILES['picture']
            profile.save()
            registreed =True

        else:
            print(profile_form.errors,user_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    context =  {
         'user_form' : user_form,
         'profile_form' : profile_form
    }
    return render(request,'auth/registration.html',context)




def index(request):
    return render(request,'auth/index.html')

def user_login(request):
    if request =='POST' :
        print('noooooooooooooooooooooooooooooooooooooooooooo!!!')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:

            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print('faild')
            return HttpResponse('Invalid login details')
    else:
        return render(request,'auth/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))