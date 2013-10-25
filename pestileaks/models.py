from django.db.models import Model, ForeignKey, CharField, IntegerField, FloatField

class Gewas(Model):
    naam = CharField(max_length=50, blank=False, null=False, unique=True)

class ToepassingsMethode(Model):
    naam = CharField(max_length=50, blank=False, null=False, unique=True)
    #identifier = CharField(max_length=10, blank=False, null=False, unique=True)

class Middel(Model):
    naam = CharField(max_length=50, blank=False, null=False, unique=True)
    toelatings_nummer = CharField(max_length=10, blank=False, null=False, unique=True)

class Aantasting(Model):
    naam = CharField(max_length=50, blank=False, null=False, unique=True)

class GebruiksRegels(Model):
    gewas = ForeignKey(Gewas, null=False, blank=False)
    middel = ForeignKey(Middel, null=False, blank=False)
    toepassings_methode = ForeignKey(ToepassingsMethode, null=False, blank=False)
    aantasting = ForeignKey(Aantasting)

    veiligheidstermijn = IntegerField(null=False)
    wachttijd_betreding = IntegerField(null=False)
    #wachttijd_teelt = models.IntegerField(null=False)

    dosering_ondergrens = FloatField(null=False)
    dosering_bovengrens = FloatField(null=False)
    #doppen
