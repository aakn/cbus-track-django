# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MapsAPIUsageCounter'
        db.create_table(u'mapsapi_mapsapiusagecounter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'mapsapi', ['MapsAPIUsageCounter'])

        # Adding model 'MapsAddressCache'
        db.create_table(u'mapsapi_mapsaddresscache', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('lng', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'mapsapi', ['MapsAddressCache'])


    def backwards(self, orm):
        # Deleting model 'MapsAPIUsageCounter'
        db.delete_table(u'mapsapi_mapsapiusagecounter')

        # Deleting model 'MapsAddressCache'
        db.delete_table(u'mapsapi_mapsaddresscache')


    models = {
        u'mapsapi.mapsaddresscache': {
            'Meta': {'object_name': 'MapsAddressCache'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'mapsapi.mapsapiusagecounter': {
            'Meta': {'object_name': 'MapsAPIUsageCounter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mapsapi']