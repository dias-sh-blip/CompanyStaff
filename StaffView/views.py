from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import FirstLevel, SecondLevel, ThirdLevel, FourthLevel, FifthLevel
 
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# получение данных из бд
def index(request):
    first_level = FirstLevel.objects.all()
    second_level = SecondLevel.objects.all()
    third_level = ThirdLevel.objects.all()
    fourth_level = FourthLevel.objects.all()
    fifth_level = FifthLevel.objects.all()
    staff = {
    "first_level": first_level,
    "second_level": second_level,
    "third_level": third_level,
    "fourth_level": fourth_level,
    "fifth_level": fifth_level
    }
    return render(request, "index.html", staff)


def staff_show(request):
    first_level = FirstLevel.objects.all()
    second_level = SecondLevel.objects.all()
    third_level = ThirdLevel.objects.all()
    fourth_level = FourthLevel.objects.all()
    fifth_level = FifthLevel.objects.all()
    staff = {
    "first_level": first_level,
    "second_level": second_level,
    "third_level": third_level,
    "fourth_level": fourth_level,
    "fifth_level": fifth_level
    }
    return render(request, "staff_show.html", staff)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"