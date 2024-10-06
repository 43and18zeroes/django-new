from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseNotFound, Http404
from django.utils.text import slugify
from django.urls import reverse

from .dummy_data import gadgets

# Create your views here.

def start_page_view(request):
    return HttpResponse("Hey, das hat doch gut funktioniert!")

def single_gadget_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("not found by me")

def single_gadget_slug_view(request, gadget_slug):
    gadget_match = None
    
    for gadget in gadgets:
        if slugify(gadget["name"]) == gadget_slug:
            gadget_match = gadget
            
    if gadget_match:
        return JsonResponse(gadget_match)
    
    raise Http404