from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.is_staff = form.cleaned_data.get('is_organisation')
            user.password1 = form.cleaned_data.get('password1')
            user.password2 = form.cleaned_data.get('password2')
            user.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно")
            return redirect("index")
        else:
            messages.error(request, "Проверьте валидность введенных данных")
            return render(request=request, template_name="register.html", context={"register_form": form})

    form = NewUserForm
    return render(request=request, template_name="register.html", context={"register_form": form})



@csrf_protect
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Добро пожаловать, '{username}'")
                return redirect("index")
            else:
                messages.error(request, "Неверный логин или пароль")
        else:
            messages.error(request, "Неверный логин или пароль")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Вы вышли из аккаунта")
    return redirect("login")

