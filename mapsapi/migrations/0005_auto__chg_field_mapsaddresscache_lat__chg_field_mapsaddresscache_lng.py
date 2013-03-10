# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MapsAddressCache.lat'
        db.alter_column(u'mapsapi_mapsaddresscache', 'lat', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3))

        # Changing field 'MapsAddressCache.lng'
        db.alter_column(u'mapsapi_mapsaddresscache', 'lng', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3))

    def backwards(self, orm):

        # Changing field 'MapsAddressCache.lat'
        db.alter_column(u'mapsapi_mapsaddresscache', 'lat', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=7))

        # Changing field 'MapsAddressCache.lng'
        db.alter_column(u'mapsapi_mapsaddresscache', 'lng', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=7))

    models = {
        u'mapsapi.mapsaddresscache': {
            'Meta': {'ordering': "['-time']", 'object_name': 'MapsAddressCache'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'mapsapi.mapsapiusagecounter': {
            'Meta': {'object_name': 'MapsAPIUsageCounter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mapsapi']