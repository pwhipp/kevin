# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Roles.id'
        db.alter_column(u'roles', 'id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))

    def backwards(self, orm):

        # Changing field 'Roles.id'
        db.alter_column(u'roles', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

    models = {
        u'step_game.actors': {
            'Meta': {'object_name': 'Actors', 'db_table': "u'actors'"},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'})
        },
        u'step_game.movies': {
            'Meta': {'object_name': 'Movies', 'db_table': "u'movies'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'rank': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'step_game.roles': {
            'Meta': {'object_name': 'Roles', 'db_table': "u'roles'"},
            'actor_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['step_game.Actors']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'movie_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['step_game.Movies']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'})
        }
    }

    complete_apps = ['step_game']