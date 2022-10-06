from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def home(request):
    return JsonResponse({'ok':True,'dashboard':'/dashboard','about':'/about','home':'/'})

def about(request):
    return JsonResponse({'page':'About','dashboard':'/dashboard','home':'/'})

def dashboard(request):
    return JsonResponse({"pages":['/about','/admin','/']})
    