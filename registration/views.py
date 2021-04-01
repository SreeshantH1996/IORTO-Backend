from django.shortcuts import render, redirect

# Create your views here.
from registration.models import Person


def home(request):
    return render(request, 'index.html')


def user_login(request):
    try:
        return render(request, 'index.html')
    except Exception as e:
        print(f"error - {e}")


def user_registration(request):
    if request.method == 'POST':
        data = request.POST
        print(data.get("name"))
        Person.objects.create(
            name=data.get("name"),
            address=data.get("address"),
            age=data.get("age"),
            district=data.get("district"),
            username=data.get("username"),
            password=data.get("password")
        )
        return redirect("home")
