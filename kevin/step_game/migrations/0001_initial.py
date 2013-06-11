# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Actors'
        db.create_table(u'actors', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1L, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['Actors'])

        # Adding model 'Directors'
        db.create_table(u'directors', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['Directors'])

        # Adding model 'DirectorsGenres'
        db.create_table(u'directors_genres', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('director_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('prob', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['DirectorsGenres'])

        # Adding model 'Movies'
        db.create_table(u'movies', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rank', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['Movies'])

        # Adding model 'MoviesDirectors'
        db.create_table(u'movies_directors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('director_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('movie_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['MoviesDirectors'])

        # Adding model 'MoviesGenres'
        db.create_table(u'movies_genres', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['MoviesGenres'])

        # Adding model 'Roles'
        db.create_table(u'roles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actor_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('movie_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['Roles'])


    def backwards(self, orm):
        # Deleting model 'Actors'
        db.delete_table(u'actors')

        # Deleting model 'Directors'
        db.delete_table(u'directors')

        # Deleting model 'DirectorsGenres'
        db.delete_table(u'directors_genres')

        # Deleting model 'Movies'
        db.delete_table(u'movies')

        # Deleting model 'MoviesDirectors'
        db.delete_table(u'movies_directors')

        # Deleting model 'MoviesGenres'
        db.delete_table(u'movies_genres')

        # Deleting model 'Roles'
        db.delete_table(u'roles')


    models = {
        u'step_game.actors': {
            'Meta': {'object_name': 'Actors', 'db_table': "u'actors'"},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1L', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'})
        },
        u'step_game.directors': {
            'Meta': {'object_name': 'Directors', 'db_table': "u'directors'"},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'})
        },
        u'step_game.directorsgenres': {
            'Meta': {'object_name': 'DirectorsGenres', 'db_table': "u'directors_genres'"},
            'director_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prob': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'step_game.movies': {
            'Meta': {'object_name': 'Movies', 'db_table': "u'movies'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'rank': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'step_game.moviesdirectors': {
            'Meta': {'object_name': 'MoviesDirectors', 'db_table': "u'movies_directors'"},
            'director_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'step_game.moviesgenres': {
            'Meta': {'object_name': 'MoviesGenres', 'db_table': "u'movies_genres'"},
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'step_game.roles': {
            'Meta': {'object_name': 'Roles', 'db_table': "u'roles'"},
            'actor_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'})
        }
    }

    complete_apps = ['step_game']