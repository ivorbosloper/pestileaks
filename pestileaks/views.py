from annoying.decorators import render_to
import json
from django.http import HttpResponse
from pestileaks.models import Gewas, GebruiksRegel, Aantasting
from collections import OrderedDict

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

@render_to('overview.html')
def overview(request):
    return {'menuitem':'overview'}

def service(request): # gewas, aantaster, ...
    #gewas = request.GET['gewas'], aantaster
    filters = {}
    if 'gewas' in request.GET:
        filters['gewas__in'] = Gewas.objects.filter(naam__icontains=request.GET['gewas'])
    if 'aantasting' in request.GET:
        filters['aantasting__in'] = Aantasting.objects.filter(naam__icontains=request.GET['aantasting'])

    
    regels = GebruiksRegel.objects.filter(**filters)
    response_data = {}
    response_data['regels'] = [ {'id':r.id, 'gewas':r.gewas.naam, 
                                 'middel': r.middel.naam, 
                                 'toepassings_methode': r.toepassings_methode.naam, 
                                 'aantasting':r.aantasting.naam,
                                 'veiligheidstermijn':r.veiligheidstermijn
                                } for r in regels]
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def _ne(dic):
    for k,v in dic.items():
        if v == None or v == '' or v == []:
            del dic[k]
    return dic

def _recurse(d, code_prefix, length):
    print "recurse %s %s" % (code_prefix, length)
    return [ _ne({'name':i.edi_naam, 'children':_recurse(d, i.edi_code, length+2)}) for i in d if i.edi_code.startswith(code_prefix) and len(i.edi_code)==length]

def gewassen(request):
    d = list(Gewas.objects.all().order_by('niveau', 'edi_code'))
    gewassen = _recurse(d, '', 1)
        
    return HttpResponse(json.dumps(gewassen), content_type="application/json")

    