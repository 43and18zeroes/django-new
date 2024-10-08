from django.urls import path
from .views import start_page_view, single_gadget_int_view, single_manufacturer_int_view, \
    single_gadget_view, add_new_man, GadgetView, ManufacturerView, RedirectToGadgetView

urlpatterns = [
    path('start/', start_page_view),
    path('', RedirectToGadgetView.as_view()),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/', GadgetView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget_int_view),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url"),
    path('gadget/<path:any_path>', GadgetView.as_view(), name="gadget_slug_url"),
    path('manufacturer/add_new_man', add_new_man, name='add_new_manufacturer'),
    path('manufacturer/<int:manufacturer_id>', single_manufacturer_int_view),
    path('manufacturer/<slug:manufacturer_slug>', ManufacturerView.as_view(), name="manufacturer_slug_url"),
    path('manufacturer/add_new_man/', ManufacturerView.as_view(), name="manufacturer_slug_url")
]
