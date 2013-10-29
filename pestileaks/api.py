from tastypie.resources import ModelResource
from models import Gewas, ToepassingsMethode, Middel, Aantasting, GebruiksRegel

class GewasResource(ModelResource):
    class Meta:
        queryset = Gewas.objects.all()

class ToepassingsMethodeResource(ModelResource):
    class Meta:
        queryset = ToepassingsMethode.objects.all()

class MiddelResource(ModelResource):
    class Meta:
        queryset = Middel.objects.all()

class AantastingResource(ModelResource):
    class Meta:
        queryset = Aantasting.objects.all()

class GebruiksRegelResource(ModelResource):
    class Meta:
        queryset = GebruiksRegel.objects.all()

