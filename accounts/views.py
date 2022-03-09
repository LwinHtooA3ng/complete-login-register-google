from multiprocessing import context
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def index(request):
    return render(request, "welcome.html", {})

@login_required
def home(request):
    return render(request, "home.html", {})

# class LoginView(auth_views.LoginView):
#     form_class = LoginForm
#     template_name = 'accounts/login.html'


# def login_view(request):

#     if request.method == "POST":
#         form = AuthenticationForm(request, data = request.POST)
#         # form = LoginForm(request.POST or None)

#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("/home")
#     else:
#         form = AuthenticationForm(request)
#         form = LoginForm(request)

#     context = {
#         "form": form
#     }
#     return render(request, "accounts/login.html", context)


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        # if user is None:
        #     context = {"error": "Invalid username or password."}
        #     form = LoginForm()
        #     return render(request, "accounts/login.html", context)
        if user is not None:
            login(request, user)
            return redirect("/home")
        context = {"error": "Invalid username or password.", "form": LoginForm(request.POST or None)}
        return render(request, "accounts/login.html", context)
        f
    return render(request, "accounts/login.html", {'form': form})

# class RegisterView(generic.CreateView):
#     form_class = RegisterForm
#     template_name = 'accounts/register.html'
#     success_url = reverse_lazy('login')

def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        form.save()
        return redirect("/login")
    return render(request, "accounts/register.html", context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})