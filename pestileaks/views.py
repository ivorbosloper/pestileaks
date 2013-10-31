from annoying.decorators import render_to
import json
from django.http import HttpResponse
from pestileaks.models import Gewas, GebruiksRegel, Aantasting, Middel
from collections import OrderedDict
import itertools

@render_to('index.html')
def index(request):
    return {'menuitem':'index'}

@render_to('app.html')
def app(request):
    return {'menuitem':'app'}

@render_to('contribute.html')
def contribute(request):
    return {'menuitem':'contribute'}

@render_to('motivation.html')
def motivation(request):
    return {'menuitem':'motivation'}

@render_to('overview.html')
def overview(request):
    return {'menuitem':'overview'}

def service(request): # gewas, aantaster, ...
    #gewas = request.GET['gewas'], aantaster
    filters = {}
    if 'gewas' in request.GET:
        filters['gewas__in'] = Gewas.objects.filter(edi_naam__icontains=request.GET['gewas'])
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

#kick empty elements from dict
def _ne(dic):
    for k,v in dic.items():
        if v == None or v == '' or v == []:
            del dic[k]
    return dic

def gewassen(request):
    def _recurse(d, code_prefix, length):
        return [ _ne({'name':i.edi_naam, 'children':_recurse(d, i.edi_code, length+2)}) for i in d if i.edi_code.startswith(code_prefix) and len(i.edi_code)==length]
    d = list(Gewas.objects.all().distinct('niveau', 'edi_naam').order_by('niveau', 'edi_naam'))
    gewassen = _recurse(d, '', 1)
        
    return HttpResponse(json.dumps(gewassen), content_type="application/json")

# group by bedrijf, doel, gewas, etc
def middelen(request):
    minsize = int(request.GET['minsize']) if request.GET['minsize'] else 0
    middel_per_bedrijf = []
    for bedrijf,iter in itertools.groupby(Middel.objects.all().order_by('bedrijf', 'naam'), lambda m: m.bedrijf):
        middelen = list(iter)
        if len(middelen) > minsize: middel_per_bedrijf.append({'name':bedrijf, 'children':[{'name': m.naam} for m in middelen]})
    return HttpResponse(json.dumps(middel_per_bedrijf), content_type="application/json")
    