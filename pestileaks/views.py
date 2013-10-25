from annoying.decorators import render_to
import json
from django.http import HttpResponse

@render_to('index.html')
def index(request):
    return {}

def service(request): # gewas, aantaster, ...
    response_data = {}
    response_data['toelating'] = 'het mag'
    return HttpResponse(json.dumps(response_data), content_type="application/json")