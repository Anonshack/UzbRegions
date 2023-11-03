from django.views.generic import ListView
from django.db.models import F
from django.http import HttpResponse

from .models import UzbRegions, UzbDistricts


# Create your views here.
class RegionsListView(ListView):
    # model = UzbRegions
    template_name = 'regions.html'

    def get_queryset(self):
        try:
            lang = self.request.session['lang']
        except:
            lang = 'uz'
            self.request.session['lang'] = 'uz'

        queryset = UzbRegions.objects.all().values('id', 'region_name_' + lang).annotate(region_name=F('region_name_'+lang))
        return queryset


class DistrictsListView(ListView):
    template_name = 'districts.html'

    def get_queryset(self):
        try:
            pk = self.request.GET['region']
        except:
            pk = 1

        try:
            lang = self.request.session['lang']
        except:
            lang = 'uz'
            self.request.session['lang'] = 'uz'

        queryset = UzbDistricts.objects.filter(district_region=pk).values('id', 'district_name_' + lang).annotate(district_name=F('district_name_'+lang))
        return queryset


def setLanguage(request, lang):
    request.session['lang'] = lang
    return HttpResponse('OK')