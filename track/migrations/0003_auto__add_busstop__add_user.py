# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BusStop'
        db.create_table(u'track_busstop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['track.RouteDetail'])),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('lon', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'track', ['BusStop'])

        # Adding model 'User'
        db.create_table(u'track_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['track.BusStop'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'track', ['User'])


    def backwards(self, orm):
        # Deleting model 'BusStop'
        db.delete_table(u'track_busstop')

        # Deleting model 'User'
        db.delete_table(u'track_user')


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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'stop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['track.BusStop']"})
        }
    }

    complete_apps = ['track']