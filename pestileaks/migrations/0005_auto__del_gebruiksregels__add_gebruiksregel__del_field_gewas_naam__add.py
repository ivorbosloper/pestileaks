# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'GebruiksRegels'
        db.delete_table('pestileaks_gebruiksregels')

        # Adding model 'GebruiksRegel'
        db.create_table('pestileaks_gebruiksregel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gewas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.Gewas'])),
            ('middel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.Middel'])),
            ('toepassings_methode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.ToepassingsMethode'])),
            ('aantasting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.Aantasting'])),
            ('veiligheidstermijn', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('wachttijd_betreding', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dosering_ondergrens', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dosering_bovengrens', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('pestileaks', ['GebruiksRegel'])

        # Deleting field 'Gewas.naam'
        db.delete_column('pestileaks_gewas', 'naam')

        # Adding field 'Gewas.niveau'
        db.add_column('pestileaks_gewas', 'niveau',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=4),
                      keep_default=False)

        # Adding field 'Gewas.code'
        db.add_column('pestileaks_gewas', 'code',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Gewas.edi_naam'
        db.add_column('pestileaks_gewas', 'edi_naam',
                      self.gf('django.db.models.fields.CharField')(default='test', max_length=50),
                      keep_default=False)

        # Adding field 'Gewas.edi_periode'
        db.add_column('pestileaks_gewas', 'edi_periode',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gewas.edi_teeltdoel'
        db.add_column('pestileaks_gewas', 'edi_teeltdoel',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gewas.teelt_onbedekt'
        db.add_column('pestileaks_gewas', 'teelt_onbedekt',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gewas.teelt_bedekt'
        db.add_column('pestileaks_gewas', 'teelt_bedekt',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gewas.teelt_opkweek_bedekt'
        db.add_column('pestileaks_gewas', 'teelt_opkweek_bedekt',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gewas.dr_gewas_object'
        db.add_column('pestileaks_gewas', 'dr_gewas_object',
                      self.gf('django.db.models.fields.CharField')(default='test', max_length=50),
                      keep_default=False)

        # Adding field 'Gewas.dr_opmerkingen_teeltdoel'
        db.add_column('pestileaks_gewas', 'dr_opmerkingen_teeltdoel',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Gewas.dr_code'
        db.add_column('pestileaks_gewas', 'dr_code',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Gewas.mest_gewas_object'
        db.add_column('pestileaks_gewas', 'mest_gewas_object',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Gewas.mest_opmerkingen_teeltdoel'
        db.add_column('pestileaks_gewas', 'mest_opmerkingen_teeltdoel',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Gewas.mest_code'
        db.add_column('pestileaks_gewas', 'mest_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'GebruiksRegels'
        db.create_table('pestileaks_gebruiksregels', (
            ('aantasting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.Aantasting'])),
            ('veiligheidstermijn', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dosering_ondergrens', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('middel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.Middel'])),
            ('wachttijd_betreding', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dosering_bovengrens', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gewas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.Gewas'])),
            ('toepassings_methode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.ToepassingsMethode'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('pestileaks', ['GebruiksRegels'])

        # Deleting model 'GebruiksRegel'
        db.delete_table('pestileaks_gebruiksregel')


        # User chose to not deal with backwards NULL issues for 'Gewas.naam'
        raise RuntimeError("Cannot reverse this migration. 'Gewas.naam' and its values cannot be restored.")
        # Deleting field 'Gewas.niveau'
        db.delete_column('pestileaks_gewas', 'niveau')

        # Deleting field 'Gewas.code'
        db.delete_column('pestileaks_gewas', 'code')

        # Deleting field 'Gewas.edi_naam'
        db.delete_column('pestileaks_gewas', 'edi_naam')

        # Deleting field 'Gewas.edi_periode'
        db.delete_column('pestileaks_gewas', 'edi_periode')

        # Deleting field 'Gewas.edi_teeltdoel'
        db.delete_column('pestileaks_gewas', 'edi_teeltdoel')

        # Deleting field 'Gewas.teelt_onbedekt'
        db.delete_column('pestileaks_gewas', 'teelt_onbedekt')

        # Deleting field 'Gewas.teelt_bedekt'
        db.delete_column('pestileaks_gewas', 'teelt_bedekt')

        # Deleting field 'Gewas.teelt_opkweek_bedekt'
        db.delete_column('pestileaks_gewas', 'teelt_opkweek_bedekt')

        # Deleting field 'Gewas.dr_gewas_object'
        db.delete_column('pestileaks_gewas', 'dr_gewas_object')

        # Deleting field 'Gewas.dr_opmerkingen_teeltdoel'
        db.delete_column('pestileaks_gewas', 'dr_opmerkingen_teeltdoel')

        # Deleting field 'Gewas.dr_code'
        db.delete_column('pestileaks_gewas', 'dr_code')

        # Deleting field 'Gewas.mest_gewas_object'
        db.delete_column('pestileaks_gewas', 'mest_gewas_object')

        # Deleting field 'Gewas.mest_opmerkingen_teeltdoel'
        db.delete_column('pestileaks_gewas', 'mest_opmerkingen_teeltdoel')

        # Deleting field 'Gewas.mest_code'
        db.delete_column('pestileaks_gewas', 'mest_code')


    models = {
        'pestileaks.aantasting': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Aantasting'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'pestileaks.gebruiksregel': {
            'Meta': {'ordering': "['gewas', 'middel', 'toepassings_methode', 'aantasting']", 'object_name': 'GebruiksRegel'},
            'aantasting': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pestileaks.Aantasting']"}),
            'dosering_bovengrens': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dosering_ondergrens': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gewas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pestileaks.Gewas']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'middel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pestileaks.Middel']"}),
            'toepassings_methode': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pestileaks.ToepassingsMethode']"}),
            'veiligheidstermijn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wachttijd_betreding': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'pestileaks.gewas': {
            'Meta': {'ordering': "['edi_naam', 'code']", 'object_name': 'Gewas'},
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'dr_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'dr_gewas_object': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dr_opmerkingen_teeltdoel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'edi_naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'edi_periode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'edi_teeltdoel': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mest_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mest_gewas_object': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mest_opmerkingen_teeltdoel': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'niveau': ('django.db.models.fields.SmallIntegerField', [], {}),
            'teelt_bedekt': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'teelt_onbedekt': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'teelt_opkweek_bedekt': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'pestileaks.middel': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Middel'},
            'bedrijf': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'eenheid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'toelatings_nummer': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'})
        },
        'pestileaks.toepassingsmethode': {
            'Meta': {'object_name': 'ToepassingsMethode'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['pestileaks']