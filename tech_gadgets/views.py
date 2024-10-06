from django.shortcuts import render
from django.http import HttpResponse
# import json
from django.http import JsonResponse
from .dummy_data import gadgets

# Create your views here.

def start_page_view(request):
    return HttpResponse("Hey, das hat doch gut funktioniert!")

def single_gadget_view(request, gadget_id):
    # return HttpResponse(json.dumps(gadget_id))
    return JsonResponse({"test": True})