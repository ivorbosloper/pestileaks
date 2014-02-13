## Zaken die handmatig eerst geregeld moeten worden
# 1. apt-get install mdb-tools
# 2. postgres db 'fytostatdb' aanmaken

## Exporteer de mdb naar sqlimport. mdb-tools zorgt niet voor een volledig goede export naar postgres
mdb-schema --drop-table dat_Fyra.mdb postgres > tmp1.sql
## Splits de sqlimport in tmp1a: create tables en zo tmp1b: constraints en indexes
cat tmp1.sql|
sed /'CREATE INDEX'/d|
sed /'Relationships'/d|
sed /'CREATE UNIQUE INDEX'/d|
sed /'ADD CONSTRAINT'/d|
## 'DROP TABLE' moet 'CASCADE' erbij hebben, omdat anders tables met constraints niet goed gaan.
sed '/DROP\ TABLE\ IF\ EXISTS/s/\(^.*\)\"\;$/\1\" CASCADE\;/g' > tmp1a.sql
cat tmp1.sql|
sed -n """ 
/CREATE\ INDEX/p;
/Relationships/p;
/CREATE\ UNIQUE\ INDEX/p;
/ADD\ CONSTRAINT/p; 
""" > tmp1b.sql

psql fytostatdb < tmp1a.sql
## Haal de namen van alle tabellen uit de db 
echo "\dt" | psql fytostatdb|awk -F "|" '{print $2}'|sed -e :a -e '$d;N;2,1ba' -e 'P;D'|sed -n '4,$p'|sed 's/^\ //g'|sed 's/[\ ]\{1,\}$//g' > tmp2
## Voeg voor elke tabel uit db de gegevens toe.
while read table;do
	echo '--------------------------'
	echo '--- '$table' --- '
	echo "delete from \"$table\";"| psql fytostatdb 
	mdb-export -I postgres -d 'QQQ' dat_Fyra.mdb "$table"|
	#maak de output van mdb-export (beter) geschikt voor import ps 
	#0. verwijder EOL's die problemen geven (bv in FytoDisclaimer)
	sed ':a;N;$!ba;s/\r\n//g'|
	#1. de problemen zitten in het deel achter 'VALUES', dus ik splits de regel hierop.
	sed 's/VALUES/\nVALUES/g'|
	#2. Er zitten comma's in het bestand en om te voorkomen dat die als veld separator gaan dienen vervang ik ze tijdelijk
	sed '/^VALUES/s/\,/RRR/g'|
	sed '/^VALUES/s/QQQ/\,/g'|
	#3. Spaties weghalen direct achter veld separator
	sed '/^VALUES/s/\,\ \{1,\}/\,/g'|
	#4. Er horen geen '' quotes voor te komen, voor de zekerheid toch even weghalen als ze er wel zijn
	sed "/^VALUES/s/'//g"|
	#5. Booleans die zonder quotes in het bestand staan (0 of 1) worden niet geimporteerd door postgres
	#   Ik kwam er toevallig achter dat als ik ze quote ('0' of '1') dat importeren wel goed gaat, vandaar vervangen.
	#   ALs er per ongeluk integers gequote worden heeft dit geen ongewenste effecten
	#   De eerste regel is omdat er soms twee booleans naast elkaar voorkomen. Let op: wat als 3 booleans naast elkaar ?
	sed "/^VALUES/s/\,\([01]\)\,\([01]\)\,/\,\'\1\'\,\'\2\'\,/g"|
	sed "/^VALUES/s/\,\([01]\)\,/\,\'\1\'\,/g"|
	#6. "" quotes worden niet geimporteerd door postgres, dus vervangen door '' quotes.
	sed "/^VALUES/s/\"/\'/g"|
	#7. commas uit punt 2. weer teruggezet.
	sed "s/RRR/\,/g"|
	#8. Lijnsplitsing op 'VALUES' uit punt 1 weer ongedaan gemaakt.
	sed ':a;N;$!ba;s/\nVALUES/VALUES/g' > tmp1.sql
	# Importeer data in db	
	psql fytostatdb < tmp1.sql
done < tmp2
## Voeg indexen/relaties uit sql toe.
psql fytostat.db < tmp1b.sql

## Exporteer de database eventueel naar sql output
pg_dump -c --no-owner fytostatdb > dat_Fyra.psql
## Ruim op
rm tmp1.sql tmp1a.sql tmp1b.sql tmp2

## Opmerkingen
#+ Als je script meer dan 1 keer draait, dan verschijnen er foutmeldingen bij het aanmaken van constraints
#  Dit komt omdat 'mdb-schema --drop-table' niet indexes en constraints verwijderd en er dan bij CREATE
#  problemen ontstaan omdat een index of constraint al bestaat. Je kunt dus het beste steeds met een nieuwe db beginnen.
