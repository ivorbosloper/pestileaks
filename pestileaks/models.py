from django.db.models import Model, ForeignKey, CharField, IntegerField, FloatField, SmallIntegerField, NullBooleanField

class Gewas(Model):
    #1       Teeltgroepen, toepassingssectoren
    #101     Gewasgroepen, toepassingsgebieden
    #10101   Sub-gewasgroep
    #1010101 Gewas
    niveau = SmallIntegerField(choices=((1,'1. Teeltgroepen, toepassingssectoren'), 
                                       (2, '2. Gewasgroepen, toepassingsgebieden'),
                                       (3, '3. Sub-gewasgroep'),
                                       (4, '4. Gewas')) )
    edi_code = CharField(max_length=10)
    edi_naam = CharField(max_length=255)
    edi_periode = CharField(max_length=50, blank=True, null=True)
    edi_teeltdoel = CharField(max_length=255, blank=True, null=True)

    teelt_onbedekt = NullBooleanField()
    teelt_bedekt = NullBooleanField()
    teelt_opkweek_bedekt = NullBooleanField()
    
    dr_gewas_object = CharField(max_length=50)
    dr_opmerkingen_teeltdoel = CharField(max_length=255)
    dr_code = IntegerField(null=True)
    
    mest_gewas_object = CharField(max_length=50)
    mest_opmerkingen_teeltdoel = CharField(max_length=255)
    mest_code = CharField(max_length=50)


    def get_parent(self):
        if self.niveau <= 1: return None
        return Gewas.objects.filter(niveau=self.niveau-1, edi_code=self.edi_code[:-2])

    def get_parent_code(self):
        if self.niveau <= 1: return None
        return self.edi_code[:-2]
    
    def __unicode__(self):
        return self.edi_naam
    
    class Meta:
        ordering = ['edi_naam','edi_code']
        verbose_name_plural = "gewassen"    

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
        verbose_name_plural = "middelen"
        
class Aantasting(Model):
    naam = CharField(max_length=50, blank=False, null=False, unique=True)

    def __unicode__(self):
        return self.naam

    class Meta:
        ordering = ['naam']
        verbose_name_plural = "aantastingen"

class GebruiksRegel(Model):
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

    class Meta:
        ordering = ['gewas', 'middel', 'toepassings_methode', 'aantasting']
        verbose_name_plural = "gebruiksregels"

