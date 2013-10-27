from django.db.models import Model, ForeignKey, CharField, IntegerField, FloatField

class Gewas(Model):
    naam = CharField(max_length=50, blank=False, null=False, unique=True)
    
    def __unicode__(self):
        return self.naam
    
    class Meta:
        ordering = ['naam']
    

class ToepassingsMethode(Model):
    naam = CharField(max_length=50, blank=False, null=False, unique=True)
    #identifier = CharField(max_length=10, blank=False, null=False, unique=True)

    def __unicode__(self):
        return self.naam

class Middel(Model):
    naam = CharField(max_length=50, blank=False, null=False)
    toelatings_nummer = CharField(max_length=10, blank=False, null=False, unique=True)
    bedrijf = CharField(max_length=50, blank=True)
    eenheid = CharField(max_length=10, blank=True)

    def __unicode__(self):
        return self.naam

    class Meta:
        ordering = ['naam']

class Aantasting(Model):
    naam = CharField(max_length=50, blank=False, null=False, unique=True)

    def __unicode__(self):
        return self.naam

    class Meta:
        ordering = ['naam']


class GebruiksRegels(Model):
    gewas = ForeignKey(Gewas, null=False, blank=False)
    middel = ForeignKey(Middel, null=False, blank=False)
    toepassings_methode = ForeignKey(ToepassingsMethode, null=False, blank=False)
    aantasting = ForeignKey(Aantasting)

    veiligheidstermijn = IntegerField(null=True, blank=True)
    wachttijd_betreding = IntegerField(null=True, blank=True)
    #wachttijd_teelt = models.IntegerField(null=False)

    dosering_ondergrens = FloatField(null=True, blank=True)
    dosering_bovengrens = FloatField(null=True, blank=True)
    #doppen

    def __unicode__(self):
        return "%s %s %s %s" % (self.gewas, self.middel, self.toepassings_methode, self.aantasting)

