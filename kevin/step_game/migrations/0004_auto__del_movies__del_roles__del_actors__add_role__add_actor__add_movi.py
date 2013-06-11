# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Movies'
        db.delete_table(u'movies')

        # Deleting model 'Roles'
        db.delete_table(u'roles')

        # Deleting model 'Actors'
        db.delete_table(u'actors')

        # Adding model 'Role'
        db.create_table(u'roles', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('actor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['step_game.Actor'])),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['step_game.Movie'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['Role'])

        # Adding model 'Actor'
        db.create_table(u'actors', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1L, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['Actor'])

        # Adding model 'Movie'
        db.create_table(u'movies', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rank', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['Movie'])


    def backwards(self, orm):
        # Adding model 'Movies'
        db.create_table(u'movies', (
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('rank', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['Movies'])

        # Adding model 'Roles'
        db.create_table(u'roles', (
            ('role', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('movie_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['step_game.Movies'])),
            ('actor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['step_game.Actors'])),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal(u'step_game', ['Roles'])

        # Adding model 'Actors'
        db.create_table(u'actors', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1L, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal(u'step_game', ['Actors'])

        # Deleting model 'Role'
        db.delete_table(u'roles')

        # Deleting model 'Actor'
        db.delete_table(u'actors')

        # Deleting model 'Movie'
        db.delete_table(u'movies')


    models = {
        u'step_game.actor': {
            'Meta': {'object_name': 'Actor', 'db_table': "u'actors'"},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'})
        },
        u'step_game.movie': {
            'Meta': {'object_name': 'Movie', 'db_table': "u'movies'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'rank': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'step_game.role': {
            'Meta': {'object_name': 'Role', 'db_table': "u'roles'"},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['step_game.Actor']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['step_game.Movie']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'})
        }
    }

    complete_apps = ['step_game']