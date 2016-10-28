from django.db.models import Model, ForeignKey, CharField, IntegerField, FloatField, SmallIntegerField, NullBooleanField, DateField
from django.db.models.fields import TextField

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
    edi_periode = CharField(max_length=50, blank=True, null=True)    #komma-gescheiden opties, TODO: n-m koppeling
    edi_teeltdoel = CharField(max_length=255, blank=True, null=True) #komma-gescheiden opties, TODO: n-m koppeling

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

class TeeltDoel(Model):
    naam = CharField(max_length=250, blank=False, null=False, unique=True)
    edi_code = CharField(max_length=10)


class CtgbToelating(Model):
   toelatingnr = IntegerField(null=True)
   middelnaam = CharField(max_length=250, blank=False, null=False)
   MAP = CharField(max_length=250, blank=False, null=False)
   toelatinghouder = CharField(max_length=250, blank=False, null=True)
   Moedertoelating = IntegerField(null=True)
   startdatum = DateField(null=True)
   expiratiedatum = DateField(null=True)
   biogewas = CharField(max_length=250, blank=False, null=True)
   werkzamestoftot = CharField(max_length=250, blank=False, null=True)
   toepassing = CharField(max_length=250, blank=False, null=True)
   pro_wcode = IntegerField(null=True)
   pro_opgebruikdatum = DateField(null=True)
   pro_afleverdatum = DateField(null=True)
   nopro_wcode = IntegerField(null=True)
   nopro_opgebruikdatum = DateField(null=True)
   nopro_afleverdatum = DateField(null=True)
   toegelaten_janee = IntegerField(null=False)

class CtgbWerkzamestof(Model):
   toelatingnr = IntegerField(null=True)
   werkzamestof = CharField(max_length=250,blank=False,null=True)

class CtgbHoeveelheid(Model):
   toelatingnr = IntegerField(null=True)
   werkzamestof = CharField(max_length=250,blank=False,null=True)
   concentratie = CharField(max_length=250,blank=False,null=True)

class ToepassingsMethode(Model):
    naam = CharField(max_length=250, blank=False, null=False, unique=True)
    #identifier = CharField(max_length=10, blank=False, null=False, unique=True)

    def __unicode__(self):
        return self.naam

class Middel(Model):
    naam = CharField(max_length=250, blank=False, null=False)
    toelatings_nummer = CharField(max_length=10, blank=False, null=False, unique=True)
    bedrijf = CharField(max_length=250, blank=True)
    eenheid = CharField(max_length=10, blank=True)

    def __unicode__(self):
        return self.naam

    class Meta:
        ordering = ['naam']
        verbose_name_plural = "middelen"
        
class Aantasting(Model):
    naam = CharField(max_length=250, blank=False, null=False, unique=True)

    def __unicode__(self):
        return self.naam

    class Meta:
        ordering = ['naam']
        verbose_name_plural = "aantastingen"

#BEDEKKING_TYPES = (("", "ongedefinieerd"), ("bedekt", "Bedekt"),("onbedekt", "Onbedekt"),)

class GebruiksRegel(Model):
    middel = ForeignKey(Middel, null=False, blank=False)

    #test = ForeignKey(Test, null=True, blank=True)  # kan denk ik weg, Rik #weggehaald, check of goed gaat!
    gewas = ForeignKey(Gewas, null=True, blank=True)
    teeltdoel = ForeignKey(TeeltDoel, null=True, blank=True)
#    bedekking = CharField(max_length=50, blank=True, null=False, choices=BEDEKKING_TYPES)
    #gewas_doel = ForeignKey(GewasDoel, null=True, blank=True)
    toepassings_methode = ForeignKey(ToepassingsMethode, null=True, blank=True)
    aantasting = ForeignKey(Aantasting, null=True, blank=True)

    filters = TextField(default='') # vrij formaat (json) filters, later oplossen/structureren

    veiligheidstermijn = IntegerField(null=True, blank=True)
    wachttijd_betreding = IntegerField(null=True, blank=True)
    #wachttijd_teelt = models.IntegerField(null=False)

    dosering_ondergrens = FloatField(null=True, blank=True)
    dosering_bovengrens = FloatField(null=True, blank=True)
    #doppen

    def __unicode__(self):
        return "%s %s %s %s" % (self.gewas, self.middel, self.toepassings_methode, self.aantasting)

    class Meta:
        #ordering = ['test', 'gewas', 'middel', 'toepassings_methode', 'aantasting']
        ordering = ['gewas', 'middel', 'toepassings_methode', 'aantasting']
        verbose_name_plural = "gebruiksregels"

