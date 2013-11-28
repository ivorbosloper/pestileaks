from pestileaks.models import GebruiksRegel, Gewas, Middel, Aantasting,\
    ToepassingsMethode, TeeltDoel
from django.core.management.base import BaseCommand

import logging
import re
import json
import os
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

#relevant ids, scraped from an unknown source
_ids = ['10002', '10098', '10135', '10172', '10194', '10211', '10262', '10274', '10318', '10319', '10372', '10379', '10423', '10450', '10560', '10568', '10572', '10602', '10645', '10701', '10710', '10766', '10768', '10784', '10793', '10866', '10867', '10903', '10904', '10945', '10946', '11003', '11004', '11014', '11019', '11078', '11198', '11222', '11227', '11228', '11230', '11234', '11264', '11291', '11341', '11393', '11407', '11408', '11429', '11432', '11453', '11455', '11483', '11503', '11526', '11529', '11533', '11553', '11557', '11567', '11585', '11599', '11651', '11662', '11687', '11709', '11754', '11765', '11767', '11824', '11826', '11841', '11885', '11894', '11955', '11958', '11962', '11995', '11996', '12015', '12059', '12063', '12096', '12128', '12130', '12148', '12175', '12204', '12205', '12216', '12228', '12229', '12236', '12277', '12279', '12282', '12283', '12285', '12289', '12346', '12353', '12361', '12371', '12379', '12394', '12407', '12409', '12411', '12413', '12417', '12421', '12423', '12431', '12432', '12433', '12440', '12448', '12452', '12456', '12468', '12477', '12491', '12497', '12504', '12516', '12517', '12518', '12519', '12521', '12537', '12545', '12551', '12552', '12557', '12585', '12592', '12602', '12610', '12629', '12630', '12661', '12665', '12667', '12678', '12679', '12692', '12696', '12697', '12698', '12707', '12709', '12723', '12725', '12737', '12746', '12747', '12748', '12749', '12755', '12757', '12762', '12776', '12781', '12783', '12787', '12809', '12813', '12818', '12819', '12824', '12836', '12843', '12849', '12859', '12866', '12869', '12873', '12877', '12878', '12899', '12915', '12920', '12921', '12922', '12926', '12927', '12930', '12942', '12951', '12960', '12968', '12969', '12970', '12975', '12982', '12988', '12990', '12994', '13007', '13044', '13057', '13066', '13070', '13077', '13087', '13089', '13129', '13137', '13142', '13144', '13145', '13148', '13150', '13152', '13168', '13185', '13186', '13197', '13207', '13211', '13217', '13220', '13225', '13229', '13234', '13235', '13257', '13258', '13268', '13275', '13287', '13290', '13299', '13314', '13317', '13372', '13389', '13401', '13404', '13413', '13422', '13467', '13477', '13479', '13489', '13490', '13497', '13502', '13513', '13514', '13530', '13531', '13555', '13561', '13575', '13576', '13578', '13579', '13580', '13582', '13586', '13593', '13601', '13628', '13722', '13774', '13775', '13794', '13795', '13796', '13797', '13799', '13802', '13805', '13813', '13830', '13832', '13848', '13853', '13863', '13864', '13865', '13881', '13883', '13884', '13898', '13905', '13944', '13947', '13949', '13952', '13976', '13978', '13982', '13983', '13984', '13985', '13986', '14012', '14027', '14097', '14159', '3014', '3019', '302702', '3039', '3045', '3059', '3109', '311401', '3117', '3135', '3136', '3137', '3141', '3150', '3178', '3201', '3207', '3209', '3219', '3221', '3225', '3229', '3235', '3236', '3237', '3238', '3246', '3250', '3252', '3262', '3270', '3272', '3274', '3275', '3290', '3300', '3317', '3322', '3333', '3334', '3355', '3357', '3363', '3367', '3368', '3371', '3374', '3384', '3386', '3390', '3391', '3395', '3397', '3400', '3992', '4001', '4015', '4034', '4050', '4187', '4285', '4372', '4379', '4859', '5122', '5134', '5282', '5581', '5582', '562', '5634', '564', '5699', '575', '5794', '582', '590', '5952', '6019', '6026', '6034', '6042', '606', '607', '608', '613', '614', '6169', '617', '6191', '6268', '6269', '6270', '6271', '6273', '6274', '628', '6284', '6290', '6304', '6305', '6306', '6308', '6309', '631', '6312', '6314', '6320', '6321', '6322', '6324', '6469', '6483', '6598', '6834', '7211', '7227', '7238', '7242', '7517', '7556', '7737', '7758', '7774', '7827', '7830', '7862', '7866', '7938', '8024', '8083', '8158', '8349', '8545', '8597', '8627', '8629', '8660', '8708', '8733', '8766', '8794', '8828', '8906', '8921', '8928', '8935', '8950', '9102', '9151', '9226', '9271', '9364', '9388', '9390', '9401', '9531', '9549', '9574', '9991']
ids = ['%05d' % int(id) for id in _ids]

def strip(s):
    return re.sub('\s+', ' ', s).strip()

def normalize(s):
    return re.sub('- ?', '', strip(s))

class Command(BaseCommand):
    def _get_gewas_teeltdoel(self, toepassingsgebied):
        teeltdoel = None
        if gewas_naam.endswith('zaadteelt'):
            teeltdoel = TeeltDoel.objects.get(naam__iexact="zaadteelt")
            gewas_naam = gewas_naam[:-len('zaadteelt')]

        m = re.match("(\w+) \((\w+)\)",gewas_naam)
        if m:
            teeltdoel = TeeltDoel.objects.get(naam__iexact=m.group(2))
            gewas_naam = m.group(1)
            
        # TODO: gewas moet edi_gewascode worden 
        gewas = Gewas.objects.get(edi_naam=gewas_naam)

        return gewas_naam, teeltdoel

    
    def parseCTGB(self):
        for f in os.listdir('doc/ctgb_html'):
            nr = re.match('\d+', f).group()
            if not nr in ids: continue
            bs = BeautifulSoup(open("doc/ctgb_html/%s" %f))

            #table strategy
            for table in bs.select('table'):
                mapping, keys, rowspans = {}, None, None
                for line in table.select('tr'):
                    tds = line.select('td')
                    if not keys:
                        keys = [normalize(v.get_text()) for v in tds]
                        rowspans = [ [] ] * len(tds)
#                        print "f%s: %s" % (nr, keys)
                    elif keys[0] == u'Toepassingsgebied':
                        for i, key in enumerate(keys):
                            if len(rowspans[i]):
                                v = rowspans[i].pop()
                            else:
                                td = tds.pop(0)
                                v = strip(td.get_text())
                                if td.get('rowspan'):
                                    rowspans[i] = [v] * (int(td['rowspan'])-1)
                            mapping[key] = v
                        
                        print "%s: %s" % (nr, json.dumps(mapping, sort_keys=True, indent=2))
                        
                        middel = Middel.objects.get(toelatings_nummer=str(int(nr)))
                        gewas_naam, teeltdoel = self._get_gewas_teeltdoel(mapping['Toepassingsgebied'])
                        
                        aantasting,c = Aantasting.objects.get_or_create(naam=mapping[u'Te bestrijden organisme'])
                        toepassings_methode_naam = mapping.get('Type toepassing') or mapping.get('Type')
                        if toepassings_methode_naam:
                            toepassings_methode,c = ToepassingsMethode.objects.get_or_create(naam=toepassings_methode_naam)
                        else:
                            toepassings_methode = None
                        GebruiksRegel.objects.get_or_create(gewas=gewas, teeltdoel=teeltdoel, middel=middel, 
                                                            aantasting=aantasting, toepassings_methode=toepassings_methode)

#                        veiligheidstermijn = IntegerField(null=True, blank=True)
#                        wachttijd_betreding = IntegerField(null=True, blank=True)



#        id_10568= {u'Maximaal aantal toepassingen per teeltcyclus': u'2',
#                   u'Toepassingsgebied': u'Bieten',
#                   u'Minimum interval tussen toepassingen in dagen': u'10',
#                   u'Te bestrijden organisme': u'eenjarige onkruiden',
#                   u'Type toepassing': u'na opkomst',
#                   u'Maximaal aantal liter middel per ha per teeltcyclus of per 12 maanden': u'5 l/ha per teeltcyclus',
#                   u'Dosering (middel) per toepassing': u'1,5 l/ha1'}
#
#        id_10319= {u'Toepassingsgebied': u'Bieten',
#                   u'Minimum interval tussen toepassingen in dagen': u'10',
#                   u'Te bestrijden organisme': u'eenjarige onkruiden',
#                   u'Maximaal aantal toepassingen per teeltcyclus of per 12 maanden': u'2 per teeltcyclus',
#                   u'Maximaal aantal liter middel per ha per teeltcyclus of per 12 maanden': u'2 l/ha per teeltcyclus',
#                   u'Type': u'na opkomst',
#                   u'Dosering (middel) per toepassing': u'0,6 l/ha1'}

            
            # no other strategies for now


    def handle(self, *args, **options):
        allOptions = ['CTGB']
        if args:
            if 'all' in args: args = allOptions
            for arg in args:
                method = getattr(self, 'parse%s' % arg[0].upper() + arg[1:], None)
                method() if method else logger.info("No handle for %s" % arg)
        else:
            logger.info("no please add at least one argument: possible choices are: %s" % ",".join(allOptions))
