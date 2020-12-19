from django.shortcuts import render
from . import models
from Vaccine_App.models import VaccineCenter
from django.views.generic import TemplateView, ListView, DetailView, View
from Vaccine_App.forms import LocationForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from django.views.generic.edit import FormMixin
# Create your views here.

class LocationView(FormMixin, ListView):
    model = models.VaccineCenter
    template_name = 'location.html'
    form_class = LocationForm
    context_object_name = 'vaccine_centers'
    def get(self, request):
        form = self.get_form()
        context = {
            'form': form,
            'inputted': False,
            'success' : False,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            loc = form.cleaned_data['loc']
        geolocator = Nominatim(user_agent= 'DjangoFetcher')
        try:
            centers = VaccineCenter.objects.all()
            for center in centers.iterator():
                loc1 = geolocator.geocode(loc)
                loc2 = geolocator.geocode(center.address)
                l1 = (loc1.latitude, loc1.longitude)
                l2 = (loc2.latitude, loc2.longitude)
                center.distance = int(round(geodesic(l1, l2).miles))
                print(center.distance)
            context = {
                'form': form,
                'inputted': True,
                'success': True,
            }
            queryset = VaccineCenter.objects.order_by('distance')
            return render(request, self.template_name, context)
        except:
            context = {
                'form': form,
                'inputted': True,
                'success': False,
            }
            return render(request, self.template_name, context)


class LoginView(View):
    template_name = 'login.html'
    # context = {
    #
    # }
    # return render(request, template_name, context)

class RegisterView(View):
    template_name = 'register.html'
    # context = {
    #
    # }
    # return render(request, template_name, context)


class DeleteView(View):
    template_name = 'delete.html'
    # context = {
    #
    # }
    # return render(request, template_name, context)

class UpdateView(View):
    template_name = 'update.html'
    # context = {
    #
    # }
    # return render(request, template_name, context)
