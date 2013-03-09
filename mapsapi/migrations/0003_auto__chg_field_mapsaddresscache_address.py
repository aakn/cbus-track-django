# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MapsAddressCache.address'
        db.alter_column(u'mapsapi_mapsaddresscache', 'address', self.gf('django.db.models.fields.CharField')(max_length=1000))

    def backwards(self, orm):

        # Changing field 'MapsAddressCache.address'
        db.alter_column(u'mapsapi_mapsaddresscache', 'address', self.gf('django.db.models.fields.CharField')(max_length=1500))

    models = {
        u'mapsapi.mapsaddresscache': {
            'Meta': {'ordering': "['-time']", 'object_name': 'MapsAddressCache'},
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