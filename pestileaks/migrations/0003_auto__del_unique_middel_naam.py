# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Middel', fields ['naam']
        db.delete_unique('pestileaks_middel', ['naam'])


    def backwards(self, orm):
        # Adding unique constraint on 'Middel', fields ['naam']
        db.create_unique('pestileaks_middel', ['naam'])


    models = {
        'pestileaks.aantasting': {
            'Meta': {'object_name': 'Aantasting'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'pestileaks.gebruiksregels': {
            'Meta': {'object_name': 'GebruiksRegels'},
            'aantasting': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pestileaks.Aantasting']"}),
            'dosering_bovengrens': ('django.db.models.fields.FloatField', [], {}),
            'dosering_ondergrens': ('django.db.models.fields.FloatField', [], {}),
            'gewas': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pestileaks.Gewas']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'middel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pestileaks.Middel']"}),
            'toepassings_methode': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pestileaks.ToepassingsMethode']"}),
            'veiligheidstermijn': ('django.db.models.fields.IntegerField', [], {}),
            'wachttijd_betreding': ('django.db.models.fields.IntegerField', [], {})
        },
        'pestileaks.gewas': {
            'Meta': {'object_name': 'Gewas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'pestileaks.middel': {
            'Meta': {'object_name': 'Middel'},
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