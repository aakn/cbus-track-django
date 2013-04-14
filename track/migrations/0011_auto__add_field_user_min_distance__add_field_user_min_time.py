# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.min_distance'
        db.add_column(u'track_user', 'min_distance',
                      self.gf('django.db.models.fields.CharField')(default='2', max_length=10),
                      keep_default=False)

        # Adding field 'User.min_time'
        db.add_column(u'track_user', 'min_time',
                      self.gf('django.db.models.fields.CharField')(default='5', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.min_distance'
        db.delete_column(u'track_user', 'min_distance')

        # Deleting field 'User.min_time'
        db.delete_column(u'track_user', 'min_time')


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
            'min_distance': ('django.db.models.fields.CharField', [], {'default': "'2'", 'max_length': '10'}),
            'min_time': ('django.db.models.fields.CharField', [], {'default': "'5'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'stop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['track.BusStop']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['track']