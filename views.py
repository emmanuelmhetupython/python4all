from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorials,TutorialCategory,TutorialSeries
from .models import PythonNews
from django.contrib.auth.forms import  AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from tinymce.widgets import TinyMCE
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def single_slug(request,single_slug):
    categories  = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        return HttpResponse(f"{single_slug} is a category!!!")
    tutorials  = [t.tutorials_slug for c in Tutorials.objects.all()]
    if single_slug in categories:
        return HttpResponse(f"{single_slug} is a category!!!")
    return HttpResponse(f"{single_slug} does not corespond to anything. ")
    


def homepage(request):
    return render(request=request,template_name="main/categories.html",context={"categories":TutorialCategory.objects.all()})
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"New account successfully created:{username}")
            login(request, user)
            messages.info(request,f"You are logged in as {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}:{form.error_messages[msg]}")
    form = NewUserForm
    return render(request,"main/register.html",context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request,"Logged out successfully")
    return redirect("main:homepage")

# code to requestss
def login_request(request):
    if request.method =='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"Your are now logged in ,Enjoy python4all")
                return redirect("main:homepage")
            else:
                messages.error(request,"Invalid username and password")
        else:
                messages.error(request,"Invalid username and password ,Please enter correct details")
              
    form = AuthenticationForm()
    return render(request,"main/login.html",context = {"form":form})


def whatwedo(request):
    return render(request=request,template_name="main/whatwedo.html")
def csscode(request):
    return render(request=request,template_name="main/csscode.html")

@login_required
def forum(request):
    return render(request=request,template_name="main/categories.html")
@login_required
def contactus(request):
    return render(request=request,template_name="main/contactus.html")
@login_required
def aboutMI(request):
    return render(request=request,template_name="main/aboutMI.html")
@login_required
def donate(request):
    return render(request=request,template_name="main/donate.html")
@login_required
def shop(request):
    return render(request=request,template_name="main/shop.html")
def menu(request):
    return render(request=request,template_name="main/menu.html")
def index(request):
    return render(request=request,template_name="main/index.html")
@login_required
def hireme(request):
    return render(request=request,template_name="main/hireme.html")