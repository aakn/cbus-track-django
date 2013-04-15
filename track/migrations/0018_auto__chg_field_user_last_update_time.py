# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'User.last_update_time'
        db.alter_column(u'track_user', 'last_update_time', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'User.last_update_time'
        db.alter_column(u'track_user', 'last_update_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    models = {
        u'track.balance': {
            'Meta': {'object_name': 'Balance'},
            'balance': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'bus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['track.RouteDetail']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'track.busstop': {
            'Meta': {'object_name': 'BusStop'},
            'bus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['track.RouteDetail']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'track.bustravellog': {
            'Meta': {'object_name': 'BusTravelLog'},
            'bus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['track.RouteDetail']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'speed': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'valid': ('django.db.models.fields.CharField', [], {'default': "'YES'", 'max_length': '30'})
        },
        u'track.routedetail': {
            'Meta': {'object_name': 'RouteDetail'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'track.user': {
            'Meta': {'object_name': 'User'},
            'gcm': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update_time': ('django.db.models.fields.DateTimeField', [], {'default': "'2012-01-01 01:00'"}),
            'min_distance': ('django.db.models.fields.CharField', [], {'default': "'2'", 'max_length': '10'}),
            'min_time': ('django.db.models.fields.CharField', [], {'default': "'5'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notify': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'stop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['track.BusStop']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['track']