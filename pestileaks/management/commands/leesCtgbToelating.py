import logging
from django.core.management.base import BaseCommand
from pestileaks.models import CtgbToelating,CtgbWerkzamestof,CtgbHoeveelheid
import xlrd
import re

logger = logging.getLogger(__name__)

def convertdate(test_date):
	import datetime,xlrd
	date_format='%d-%m-%Y'
	try:
		str(float(test_date))
		datetuple=xlrd.xldate_as_tuple(float(test_date),0)
		my_date=str(datetime.date(datetuple[0],datetuple[1],datetuple[2]))
	except:
		try:
			datetime.datetime.strptime(test_date, date_format)
			my_date=test_date[6]+test_date[7]+test_date[8]+test_date[9]+'-'+test_date[3]+test_date[4]+'-'+test_date[0]+test_date[1]
		except:
			my_date=None
	return my_date

def mkint(mystring):
	if (mystring not in [None,'']):
		b = int(float(mystring))
	else:
		b = None
	return b

class Command(BaseCommand):


    def handle(self, *args, **options):
	docs = [['toegelaten_middelen.xlsx',1,'toegelaten_middelen.xls'],['vervallen_middelen.xlsx',0,'vervallen_middelen']]

	for i in docs:
		doc = xlrd.open_workbook("doc/ctgb_xls/"+i[0])
	        for sheet in doc.sheets():
			if (sheet.name==i[2]):
				for rx in range(1, sheet.nrows):
					toelatingnr = sheet.cell_value(rx,0)
					middelnaam = sheet.cell_value(rx,1)
					MAP = sheet.cell_value(rx,3)
					a=sheet.cell_value(rx,4)
					Moedertoelating = mkint(a)
					toelatinghouder = sheet.cell_value(rx,5)
					startdatum = convertdate(sheet.cell_value(rx,6))
					expiratiedatum = convertdate(sheet.cell_value(rx,7))
					biogewas = sheet.cell_value(rx,8)
					werkzamestoftot = sheet.cell_value(rx,9)
					print 'wz=',werkzamestoftot
					lista=werkzamestoftot.split(' # ',)
					print 'lista=',lista # [u'piperonylbutoxide 0,075%', u'pyrethrinen 0,03%']
					b=0
					while (b<len(lista)):
						print 'b=',b
						lista1=re.split(r', (?=[0-9])',lista[b].lstrip())
						print 'lista1=',lista1 
						if ('mengsel van:' not in lista1[0]):
							lista11=re.split(r" (?=[0-9])",lista1[0])
						else:
							lista11=[lista1[0],None]
						werkzamestof=lista11[0]
						if (len(lista11)>1):
							concentratie=lista11[1]
						else:
							concentratie=None
						print 'werkzamestof=',werkzamestof
						print 'conc=',concentratie
						CtgbWerkzamestof.objects.create(toelatingnr=toelatingnr,werkzamestof=werkzamestof)
						CtgbHoeveelheid.objects.create(toelatingnr=toelatingnr,werkzamestof=werkzamestof,concentratie=concentratie)
						c=1
						print 'lenlista1=',len(lista1)
						print 'c=',c
						while (c<len(lista1)):
							lista11=re.split(r", (?=[0-9])",lista1[c])
							for concentratie in lista11:
								print 'conc2=',concentratie
								CtgbHoeveelheid.objects.create(toelatingnr=toelatingnr,werkzamestof=werkzamestof,concentratie=concentratie)
							c=c+1
						b=b+1
					toepassing = sheet.cell_value(rx,10)
					print 'prowcode1=',sheet.cell_value(rx,11)
					a = sheet.cell_value(rx,11)
					pro_wcode= mkint(a)
					print 'prowcode2=',pro_wcode
					pro_opgebruikdatum = convertdate(sheet.cell_value(rx,12))
					pro_afleverdatum = convertdate(sheet.cell_value(rx,13))
					nopro_wcode = convertdate(sheet.cell_value(rx,14))
					nopro_opgebruikdatum = convertdate(sheet.cell_value(rx,15))
					nopro_afleverdatum = convertdate(sheet.cell_value(rx,16))
					toegelaten_janee = i[1] 
					CtgbToelating.objects.create(\
					toelatingnr=toelatingnr,\
					middelnaam=middelnaam,\
					MAP=MAP,Moedertoelating=Moedertoelating,\
					toelatinghouder=toelatinghouder,\
					startdatum=startdatum,\
					expiratiedatum=expiratiedatum,\
					biogewas=biogewas,\
					werkzamestoftot=werkzamestoftot,\
					toepassing=toepassing,\
					pro_wcode=pro_wcode,\
					pro_opgebruikdatum=pro_opgebruikdatum,\
					pro_afleverdatum=pro_afleverdatum,\
					nopro_wcode=pro_wcode,\
					nopro_opgebruikdatum=pro_opgebruikdatum,\
					nopro_afleverdatum=pro_afleverdatum,\
					toegelaten_janee=toegelaten_janee)



 
