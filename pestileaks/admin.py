from django.contrib import admin
from pestileaks.models import Gewas, GebruiksRegel, Aantasting,\
    ToepassingsMethode, Middel

admin.site.register(Gewas)
admin.site.register(ToepassingsMethode)
admin.site.register(Middel)
admin.site.register(Aantasting)
admin.site.register(GebruiksRegel)

