import logging
from django.core.management.base import BaseCommand
from pestileaks.models import Middel
import requests
import unicodecsv

logger = logging.getLogger(__name__)
BASE_URL = "http://www.ctgb.nl/ctb_files/"
FormuleringNaarEenheid = {
    'granulaat of korrel': 'kg/ha',
    'Granulaat': 'kg/ha',
    'Suspensie concentraat': 'l/ha',
    'vloeistof': 'l/ha',
    'Wateroplosbaar poeder': 'kg/ha',
    'Wateroplosbaar granulaat': 'kg/ha',
    'Spuitpoeder': 'kg/ha',
    'Met water mengbaar concentraat': 'l/ha',
    'Andere vloeistoffen voor directe toepassing': 'l/ha',
    'lokaas': 'kg/ha',
    'Tablet': 'kg/ha',
    'Emulgeerbaar concentraat': 'l/ha',
    'Water dispergeerbaar granulaat': 'kg/ha',
    'doekje': 'kg/ha',
    'Lokmiddel op graanbasis': 'kg/ha',
    'Lokmiddel (klaar voor gebruik)': 'kg/ha',
    'Gas (onder druk)': 'l/ha',
    'pompspray': 'l/ha',
    'Suspensie concentraat voor zaadbehandeling': 'l/ha',
    'Pasta op waterbasis': '',
    'Stuifpoeder': 'kg/ha',
    'Aerosol spuitbus': '',  # geen idee
    'Water dispergeerbaar poeder voor vochtige zaadbehandeling': 'kg/ha',
    'tablet': 'kg/ha',
    'Emulsie, olie in water': 'l/ha',
    'Oplossing voor plaatselijke huidbehandeling': 'l/ha',
    'Strooipoeder': 'kg/ha',
    'Tablet en Granulaat': 'kg/ha',
    'Damp ontwikkelend product': '',  # kg of l, stoffen: m of kg
    'Diversen': 'kg/ha',
    'Lokmiddel in korrelvorm': 'kg/ha',
    'Lokmiddel in blokvorm': 'kg/ha',
    'vloeibaar': 'l/ha',
    'Plantenstaafje': '',
    'Capsule suspensie': 'l/ha',
    'Emulsie voor zaadbehandeling': '',
    'Emulsie, water in olie': 'l/ha',
    'poeder': 'kg/ha',
    'Fijn granulaat': 'kg/ha',
    'Suspo-emulsie': 'l/ha',
    'Olie dispersie': '',
    'Oplossing voor ULV toepassing': 'l/ha',
    'Dispergeerbaar concentraat': 'l/ha',
    'Filmvormer': 'l/ha',
    'Koud vernevelbaar concentraat': 'l/ha',
    'Wateroplosbaar tablet': 'kg/ha',
    'Contact vloeistof of gel': '',
    'Heet vernevelbaar concentraat': 'l/ha',
    'Micro emulsie': '',
    'capsule': '',  # geen idee
    'Combiverpakking vloeibaar/vloeibaar': 'l/ha',
    'Andere poeders': 'kg/ha',
    'Ingekapseld granulaat': 'kg/ha',
    'Poeder voor droge zaadbehandeling': 'kg/ha',
    'schubben': 'kg/ha',
    'Rookontwikkelaar': 'kg/ha',
    'verspuitbaar poeder': 'kg/ha',
    'Gasontwikkelend product': 'kg/ha',
    'Technisch concentraat': 'l/ha',
    'Oplossing voor zaadbehandeling': 'l/ha',
    'rookmiddel': '',
    'aerosol': '',
    'patroon': '',
    'pasta': '',
    'staaf': '',
    'verstuiver': '',
    'stift': '',
    'oormerk': '',
    'geimpregneerde (poreuze) plaat': '',
    'strip': '',
    'verdampingsmiddel': '',
    'halsband': '',
    'gas': '',
    'plug': '',
    'gel': '',
    'tube': '',
    'suspensie': 'l/ha',
    'Concentraat voor lokmiddel': 'l/ha',
    'Rooktablet': '',  # geen idee
    'Rookpatroon': '',  # geen idee
    'Emulgeerbaar granulaat': 'kg/ha',
    'Microgranulaat': 'kg/ha',
    'Olie mengbaar concentraat': 'l/ha'}


class Command(BaseCommand):

    def handle(self, *args, **options):
        lists = {}

        for f in ["toegelaten_middelen", "vervallen_middelen"]:
            url = "%s%s.xls" % (BASE_URL, f)
            r = requests.get(url, stream=True)
            if r.status_code != 200:
                raise Exception("Kan bestand niet ophalen bij ctgb: %s" % url)
            reader = unicodecsv.DictReader(r.raw, encoding='LATIN-1', delimiter='\t', quotechar='"')
            lists[f] = list(reader)

        for f, lst in lists.items():
            for row in lst:
#                if not 'professioneel' in row['toepassing'].lower().replace('niet-professioneel', ''):
#                    continue
                formulering = row['formulering']
                formulering_eenheid = FormuleringNaarEenheid.get(formulering, None)
                eenheid = formulering_eenheid or 'l/ha'

                middel = Middel.objects.filter(toelatings_nummer=row['toelatingnr'])
                middel = middel[0] if middel else Middel()

                # # (id, naam, toelatings_nummer, bedrijf, eenheid)
                middel.naam = unicode(row['middelnaam'][:50]).capitalize()
                middel.eenheid = eenheid
                middel.toelatings_nummer = row['toelatingnr']
                middel.bedrijf = row['toelatinghouder'][:50]
                # middel.vervallen = (file == 'vervallen_middelen')
                middel.save()

            logger.info("Updated %d items for list %s" % (len(lst), f))

