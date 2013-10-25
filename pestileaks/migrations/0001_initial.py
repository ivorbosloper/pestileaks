# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gewas'
        db.create_table('pestileaks_gewas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('pestileaks', ['Gewas'])

        # Adding model 'ToepassingsMethode'
        db.create_table('pestileaks_toepassingsmethode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('pestileaks', ['ToepassingsMethode'])

        # Adding model 'Middel'
        db.create_table('pestileaks_middel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('toelatings_nummer', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
        ))
        db.send_create_signal('pestileaks', ['Middel'])

        # Adding model 'Aantasting'
        db.create_table('pestileaks_aantasting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('pestileaks', ['Aantasting'])

        # Adding model 'GebruiksRegels'
        db.create_table('pestileaks_gebruiksregels', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gewas', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.Gewas'])),
            ('middel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.Middel'])),
            ('toepassings_methode', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.ToepassingsMethode'])),
            ('aantasting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pestileaks.Aantasting'])),
            ('veiligheidstermijn', self.gf('django.db.models.fields.IntegerField')()),
            ('wachttijd_betreding', self.gf('django.db.models.fields.IntegerField')()),
            ('dosering_ondergrens', self.gf('django.db.models.fields.FloatField')()),
            ('dosering_bovengrens', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('pestileaks', ['GebruiksRegels'])


    def backwards(self, orm):
        # Deleting model 'Gewas'
        db.delete_table('pestileaks_gewas')

        # Deleting model 'ToepassingsMethode'
        db.delete_table('pestileaks_toepassingsmethode')

        # Deleting model 'Middel'
        db.delete_table('pestileaks_middel')

        # Deleting model 'Aantasting'
        db.delete_table('pestileaks_aantasting')

        # Deleting model 'GebruiksRegels'
        db.delete_table('pestileaks_gebruiksregels')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'toelatings_nummer': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'})
        },
        'pestileaks.toepassingsmethode': {
            'Meta': {'object_name': 'ToepassingsMethode'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['pestileaks']