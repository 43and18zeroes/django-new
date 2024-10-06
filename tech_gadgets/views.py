from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.text import slugify

from .dummy_data import gadgets

# Create your views here.

def start_page_view(request):
    return HttpResponse("Hey, das hat doch gut funktioniert!")

def single_gadget_view(request, gadget_id):
    return JsonResponse({"result": slugify(gadgets[1]['name'])})

def single_gadget_slug_view(request, gadget_slug):
    gadget_match = {"result": "nothing"}
    
    for gadget in gadgets:
        if slugify(gadget["name"]) == gadget_slug:
            gadget_match = gadget
            
    return JsonResponse(gadget_match)