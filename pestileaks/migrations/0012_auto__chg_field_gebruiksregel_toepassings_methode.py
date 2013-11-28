# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GebruiksRegel.toepassings_methode'
        db.alter_column(u'pestileaks_gebruiksregel', 'toepassings_methode_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.ToepassingsMethode'], null=True))

    def backwards(self, orm):

        # Changing field 'GebruiksRegel.toepassings_methode'
        db.alter_column(u'pestileaks_gebruiksregel', 'toepassings_methode_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['pestileaks.ToepassingsMethode']))

    models = {
        u'pestileaks.aantasting': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Aantasting'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'pestileaks.gebruiksregel': {
            'Meta': {'ordering': "['gewas', 'middel', 'toepassings_methode', 'aantasting']", 'object_name': 'GebruiksRegel'},
            'aantasting': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pestileaks.Aantasting']"}),
            'dosering_bovengrens': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dosering_ondergrens': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'gewas': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pestileaks.Gewas']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'middel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pestileaks.Middel']"}),
            'toepassings_methode': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pestileaks.ToepassingsMethode']", 'null': 'True', 'blank': 'True'}),
            'veiligheidstermijn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wachttijd_betreding': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'pestileaks.gewas': {
            'Meta': {'ordering': "['edi_naam', 'edi_code']", 'object_name': 'Gewas'},
            'dr_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'dr_gewas_object': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'dr_opmerkingen_teeltdoel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'edi_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'edi_naam': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'edi_periode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'edi_teeltdoel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mest_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mest_gewas_object': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mest_opmerkingen_teeltdoel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'niveau': ('django.db.models.fields.SmallIntegerField', [], {}),
            'teelt_bedekt': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'teelt_onbedekt': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'teelt_opkweek_bedekt': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'pestileaks.middel': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Middel'},
            'bedrijf': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'eenheid': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'toelatings_nummer': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'})
        },
        u'pestileaks.toepassingsmethode': {
            'Meta': {'object_name': 'ToepassingsMethode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['pestileaks']