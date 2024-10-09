import json

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseNotFound, Http404
from django.utils.text import slugify
from django.urls import reverse

from django.views import View

from .dummy_data import gadgets, manufacturers

from django.views.generic.base import RedirectView

# Create your views here.

def start_page_view(request):
    return render(request, 'tech_gadgets/test.html', {'gadget_list': gadgets})

class RedirectToGadgetView(RedirectView):
    pattern_name = "gadget_slug_url"
    
    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(gadgets[kwargs.get("gadget_id", 0)]["name"])
        new_kwargs = {"gadget_slug": slug}
        print(type(new_kwargs))
        return super().get_redirect_url(*args, **new_kwargs)

def single_gadget_int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("not found by me")

class RedirectToManufacturerView(RedirectView):
    pattern_name = "manufacturer_slug_url"
    
    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(manufacturers[kwargs.get("manufacturer_id", 0)]["name"])
        new_kwargs = {"manufacturer_slug": slug}
        print(type(new_kwargs))
        return super().get_redirect_url(*args, **new_kwargs)

def single_manufacturer_int_view(request, manufacturer_id):
    print("manufacturer_id", manufacturer_id)
    if len(manufacturers) > manufacturer_id:
        new_slug = slugify(manufacturers[manufacturer_id]["name"])
        new_url = reverse("manufacturer_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("not found by me")

class GadgetView(View):
    def get(self, request, gadget_slug):
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget
                
        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data["test"]}")
            return JsonResponse({"response": "Success GadgetView(View)"})
        except:
            return JsonResponse({"response": "Failure GadgetView(View)"})
        
class ManufacturerView(View):
    def get(self, request, manufacturer_slug):
        print("get", manufacturer_slug)
        manufacturer_match = None
        for manufacturer in manufacturers:
            if slugify(manufacturer["name"]) == manufacturer_slug:
                manufacturer_match = manufacturer
                
        if manufacturer_match:
            return JsonResponse(manufacturer_match)
        raise Http404()
    
    def post(self, request, *args, **kwargs):
        # try:
        #     data = json.loads(request.body)
        #     print(f"recieved data: {data["test"]}")
        #     return JsonResponse({"response": "Success ManufacturerView(View)"})
        # except:
        #     return JsonResponse({"response": "Failure ManufacturerView(View)"})
        
        print(request)
        if request.method == "POST":
            try:
                data = json.loads(request.body)
                name = data.get('name')
                headquarters = data.get('headquarters')
                founded = data.get('founded')
                website = data.get('website')
                description = data.get('description')

                # Hier würdest du die Daten verarbeiten oder in der Datenbank speichern
                # Beispiel: Manufacturer.objects.create(...)

                return JsonResponse({"message": "Manufacturer erfolgreich erstellt"}, status=201)
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=400)

        return JsonResponse({"error": "Invalid request method"}, status=405)

def single_gadget_view(request, gadget_slug=""):
    
    if request.method == "GET":
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget
                
        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()
    
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data["test"]}")
            return JsonResponse({"response": "Success single_gadget_view(request, gadget_slug="")"})
        except:
            return JsonResponse({"response": "Failure single_gadget_view(request, gadget_slug="")"})

def single_gadget_post_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data["test"]}")
            return JsonResponse({"response": "Success single_gadget_post_view(request)"})
        except:
            return JsonResponse({"response": "Failure single_gadget_post_view(request)"})
        
def add_new_man(request):
    print(request)
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get('name')
            headquarters = data.get('headquarters')
            founded = data.get('founded')
            website = data.get('website')
            description = data.get('description')

            # Hier würdest du die Daten verarbeiten oder in der Datenbank speichern
            # Beispiel: Manufacturer.objects.create(...)

            return JsonResponse({"message": "Manufacturer erfolgreich erstellt"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)