import logging
from django.core.management.base import BaseCommand
from pestileaks.models import Gewas
import xlrd
import re

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        doc = xlrd.open_workbook("doc/dtg/EdiTeelt_DR_Mestwet_gewassen.xls")
        for sheet in doc.sheets():
            # read all rows from 3
            for rx in range(2, sheet.nrows):
                if not sheet.cell_value(rx, 4): continue
                print "sheet.name == %s" % sheet.name
                skip_hij = 3 if sheet.name == '7. Diversen' else 0
                
                # scan first 3 cells for groups
                for i in range(3):
                    group = sheet.cell_value(rx, i)
                    if group and re.search('\s+', group):
                        code, naam = re.split('\s+', group, 1)
                        if code.endswith('.'):
                            code = code[:-1]
                        edi_code = code.replace('.','0')
                        print dict(edi_code=edi_code, edi_naam=naam, niveau=i+1)
                        Gewas.objects.create(edi_code=edi_code, edi_naam=naam, niveau=i+1)

                print dict(niveau=4, 
                                     edi_code=sheet.cell_value(rx, 4), 
                                     edi_naam=sheet.cell_value(rx, 3), 
                                     edi_periode=sheet.cell_value(rx, 5),
                                     edi_teeltdoel=sheet.cell_value(rx, 6),
                                     
#                                     teelt_onbedekt=sheet.cell_value(rx, 7) != '',
#                                     teelt_bedekt=sheet.cell_value(rx, 8) != '',
#                                     teelt_opkweek_bedekt=sheet.cell_value(rx, 9) != '',

                                     dr_gewas_object = sheet.cell_value(rx, 10-skip_hij),
                                     dr_opmerkingen_teeltdoel = sheet.cell_value(rx, 11-skip_hij),
                                     dr_code = sheet.cell_value(rx, 12-skip_hij),

                                     mest_gewas_object = sheet.cell_value(rx, 13-skip_hij),
                                     mest_opmerkingen_teeltdoel = sheet.cell_value(rx, 14-skip_hij),
                                     mest_code = sheet.cell_value(rx, 15-skip_hij))
                

                Gewas.objects.create(niveau=4, 
                                     edi_code=str(int(sheet.cell_value(rx, 4))), 
                                     edi_naam=sheet.cell_value(rx, 3), 
                                     edi_periode=sheet.cell_value(rx, 5),
                                     edi_teeltdoel=sheet.cell_value(rx, 6),
                                     
#                                     teelt_onbedekt=sheet.cell_value(rx, 7) != '',
#                                     teelt_bedekt=sheet.cell_value(rx, 8) != '',
#                                     teelt_opkweek_bedekt=sheet.cell_value(rx, 9) != '',

                                     dr_gewas_object = sheet.cell_value(rx, 10-skip_hij),
                                     dr_opmerkingen_teeltdoel = sheet.cell_value(rx, 11-skip_hij),
                                     dr_code = int(sheet.cell_value(rx, 12-skip_hij)),

                                     mest_gewas_object = sheet.cell_value(rx, 13-skip_hij),
                                     mest_opmerkingen_teeltdoel = sheet.cell_value(rx, 14-skip_hij),
                                     mest_code = sheet.cell_value(rx, 15-skip_hij))
                
