import json

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from drf_project.mixins import JsonResponseMixin

from .models import Update


# def detail_view(request):
#     return render() #return JSON data or XML

def update_model_detail_view(request):
    """
    URI -- for a REST API
    GET -- Retrieve
    """
    data = {
        "count": 100,
        "some": "something",
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "classBasedView" : "yeah!",
            "thanks":"yeah!!!!",
        }
        return JsonResponse(data)

class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "classBasedView" : "yeah!",
            "thanks":"from Json CBV2 yeah!!!!",
        }
        return self.render_to_json_response(data)


class SerializedDetailView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')

class SerializedListView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        json_data = serialize("json", qs)
        return HttpResponse(json_data, content_type='application/json')