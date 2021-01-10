from django.shortcuts import render
from django.http import JsonResponse

def home_api(request):
    data = {
        "name" : "Ally",
        "address" : "clarusway.com",
        "skills" : ["python", "django"]
    }
    return JsonResponse(data)
# Create your views here.
