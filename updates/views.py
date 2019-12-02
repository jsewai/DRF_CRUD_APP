from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Update

# def detail_view(request):
#     return render() #return JSON data or XML

def update_model_detail_view(request):
    data = {
        "count": 100,
        "some": "something",
    }
    return JsonResponse(data)