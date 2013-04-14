# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'User.stop'
        db.alter_column(u'track_user', 'stop_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['track.BusStop'], null=True))
        # Adding unique constraint on 'User', fields ['gcm']
        db.create_unique(u'track_user', ['gcm'])


    def backwards(self, orm):
        # Removing unique constraint on 'User', fields ['gcm']
        db.delete_unique(u'track_user', ['gcm'])


        # Changing field 'User.stop'
        db.alter_column(u'track_user', 'stop_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['track.BusStop']))

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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'stop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['track.BusStop']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['track']