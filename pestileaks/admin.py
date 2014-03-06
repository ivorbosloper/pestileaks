from django.contrib import admin
from pestileaks.models import CtgbToelating, CtgbWerkzamestof, CtgbHoeveelheid, Gewas, GebruiksRegel, Aantasting,\
    ToepassingsMethode, Middel

admin.site.register(CtgbToelating)
admin.site.register(CtgbWerkzamestof)
admin.site.register(CtgbHoeveelheid)
admin.site.register(Gewas)
admin.site.register(ToepassingsMethode)
admin.site.register(Middel)
admin.site.register(Aantasting)
admin.site.register(GebruiksRegel)

