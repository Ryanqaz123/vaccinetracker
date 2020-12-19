from django.shortcuts import render
from . import models
from Vaccine_App.models import VaccineCenter
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView
from Vaccine_App.forms import LocationForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from django.views.generic.edit import FormMixin
# Create your views here.

class LocationView(FormMixin, ListView):
    model = models.VaccineCenter
    template_name = 'location.html'
    form_class = LocationForm
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
                center.latitude = str(loc2.latitude)
                center.longitude = str(loc2.longitude)
                l1 = (loc1.latitude, loc1.longitude)
                l2 = (loc2.latitude, loc2.longitude)
                center.distance = int(round(geodesic(l1, l2).miles))
                center.save()

            vaccine_centers = sorted(VaccineCenter.objects.all(), key= lambda n: n.distance)
            context = {
                'form': form,
                'inputted': True,
                'success': True,
                'vaccine_centers': vaccine_centers,
                }

            return render(request, self.template_name, context)
        except:
            context = {
                'form': form,
                'inputted': True,
                'success': False,
            }
            return render(request, self.template_name, context)
