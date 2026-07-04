from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import RegisterForm, LoginForm


def auth_page(request):

    login_form = LoginForm()
    register_form = RegisterForm()

    if request.method == "POST":

        # 🔥 ثبت نام
        if "register_submit" in request.POST:

            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()

                # می‌تونی بعد ثبت‌نام مستقیم لاگین کنی (اختیاری)
                return redirect("request.META.get('HTTP_REFERER', 'products:home'")  # همون صفحه

        # 🔥 ورود
        elif "login_submit" in request.POST:

            login_form = LoginForm(request.POST)

            if login_form.is_valid():

                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]

                user = authenticate(
                    request,
                    username=username,
                    password=password
                )

                if user:
                    login(request, user)
                    return redirect("products:home")

    return render(request, "accounts/auth.html", {
        "login_form": login_form,
        "register_form": register_form,
    })


def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'products:home'))