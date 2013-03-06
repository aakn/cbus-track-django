# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RouteDetail'
        db.create_table(u'track_routedetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'track', ['RouteDetail'])

        # Adding model 'Balance'
        db.create_table(u'track_balance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['track.RouteDetail'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('balance', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'track', ['Balance'])

        # Adding model 'BusTravelLog'
        db.create_table(u'track_bustravellog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bus', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['track.RouteDetail'])),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('lon', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('speed', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('bal', self.gf('django.db.models.fields.CharField')(max_length=15000)),
        ))
        db.send_create_signal(u'track', ['BusTravelLog'])


    def backwards(self, orm):
        # Deleting model 'RouteDetail'
        db.delete_table(u'track_routedetail')

        # Deleting model 'Balance'
        db.delete_table(u'track_balance')

        # Deleting model 'BusTravelLog'
        db.delete_table(u'track_bustravellog')


    models = {
        u'track.balance': {
            'Meta': {'object_name': 'Balance'},
            'balance': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'bus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['track.RouteDetail']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'track.bustravellog': {
            'Meta': {'object_name': 'BusTravelLog'},
            'bal': ('django.db.models.fields.CharField', [], {'max_length': '15000'}),
            'bus': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['track.RouteDetail']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'speed': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'track.routedetail': {
            'Meta': {'object_name': 'RouteDetail'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['track']