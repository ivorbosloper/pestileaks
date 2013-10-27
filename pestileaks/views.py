from annoying.decorators import render_to
import json
from django.http import HttpResponse
from pestileaks.models import Gewas, GebruiksRegels, Aantasting

@render_to('index.html')
def index(request):
    return {'menuitem':'index'}

@render_to('index.html')
def app(request):
    return {'menuitem':'app'}

@render_to('index.html')
def contribute(request):
    return {'menuitem':'contribute'}

@render_to('index.html')
def motivation(request):
    return {'menuitem':'motivation'}

@render_to('index.html')
def overview(request):
    return {'menuitem':'overview'}

def service(request): # gewas, aantaster, ...
    #gewas = request.GET['gewas'], aantaster
    filters = {}
    if 'gewas' in request.GET:
        filters['gewas__in'] = Gewas.objects.filter(naam__icontains=request.GET['gewas'])
    if 'aantasting' in request.GET:
        filters['aantasting__in'] = Aantasting.objects.filter(naam__icontains=request.GET['aantasting'])

    
    regels = GebruiksRegels.objects.filter(**filters)
    response_data = {}
    response_data['regels'] = [ {'id':r.id, 'gewas':r.gewas.naam, 
                                 'middel': r.middel.naam, 
                                 'toepassings_methode': r.toepassings_methode.naam, 
                                 'aantasting':r.aantasting.naam,
                                 'veiligheidstermijn':r.veiligheidstermijn
                                } for r in regels]
    return HttpResponse(json.dumps(response_data), content_type="application/json")