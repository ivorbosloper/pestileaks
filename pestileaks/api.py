from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from models import CtgbToelating, CtgbWerkzamestof, , Gewas, ToepassingsMethode, Middel, Aantasting, GebruiksRegel
from django.db.models import Q
import operator

class QModelResource(ModelResource):
    def apply_filters(self, request, applicable_filters):
        object_list = super(QModelResource, self).apply_filters(request, applicable_filters)
        query = request.GET.get('query', None)
        if query:
            fields = [f for f in self._meta.filtering.keys() if f not in applicable_filters]
            if fields:
                qset = reduce(operator.or_, [Q((f+'__icontains',query)) for f in fields])
                object_list = object_list.filter(qset)
        return object_list

class GewasResource(ModelResource):
    class Meta:
        queryset = Gewas.objects.all()
        ordering=['id', 'naam']
        filtering = {
            'naam': ALL,
        }

class CtgbToelatingResource(ModelResource):
	class Meta:
		queryset = CtgbToelating.objects.all()
		ordering=['toelatingnr', 'middelnaam','toelatinghouder','MAP','Moedertoelating']

class CtgbWerkzamestofResource(ModelResource):
	class Meta:
		queryset = CtgbWerkzamestof.objects.all()

class CtgbHoeveelheidResource(ModelResource):
	class Meta:
		queryset = CtgbHoeveelheid.objects.all()
        
class ToepassingsMethodeResource(ModelResource):
    class Meta:
        queryset = ToepassingsMethode.objects.all()
        ordering=['id', 'naam']

class MiddelResource(QModelResource):
    class Meta:
        queryset = Middel.objects.all()
        ordering=['id', 'naam', 'bedrijf', 'toelatings_nummer']
        filtering = {
            'naam': ALL,
            'bedrijf': ALL,
            'toelatings_nummer': ALL
        }

class AantastingResource(ModelResource):
    class Meta:
        queryset = Aantasting.objects.all()

class GebruiksRegelResource(ModelResource):
    class Meta:
        queryset = GebruiksRegel.objects.all()

