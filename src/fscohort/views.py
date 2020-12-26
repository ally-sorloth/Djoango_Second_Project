from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm

def home_view(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    # print(request.method)
    form = StudentForm()
    my_context = {
        'title' : 'clarusway',
        'dict_1': {'django': 'best framework'},
        'my_list': [2, 3, 4, 5],
        'cat': 'maviş',
        'from': form
    }
    return render (request, "fscohort/home.html", my_context)

# Create your views here.

def about_view(request):
    return HttpResponse("About Page")