# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'DirectorsGenres'
        db.delete_table(u'directors_genres')

        # Deleting model 'MoviesGenres'
        db.delete_table(u'movies_genres')

        # Deleting model 'MoviesDirectors'
        db.delete_table(u'movies_directors')

        # Deleting model 'Directors'
        db.delete_table(u'directors')


        # Renaming column for 'Roles.movie_id' to match new field type.
        db.rename_column(u'roles', 'movie_id', 'movie_id_id')
        # Changing field 'Roles.movie_id'
        db.alter_column(u'roles', 'movie_id_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['step_game.Movies']))
        # Adding index on 'Roles', fields ['movie_id']
        db.create_index(u'roles', ['movie_id_id'])


        # Renaming column for 'Roles.actor_id' to match new field type.
        db.rename_column(u'roles', 'actor_id', 'actor_id_id')
        # Changing field 'Roles.actor_id'
        db.alter_column(u'roles', 'actor_id_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['step_game.Actors']))
        # Adding index on 'Roles', fields ['actor_id']
        db.create_index(u'roles', ['actor_id_id'])


    def backwards(self, orm):
        # Removing index on 'Roles', fields ['actor_id']
        db.delete_index(u'roles', ['actor_id_id'])

        # Removing index on 'Roles', fields ['movie_id']
        db.delete_index(u'roles', ['movie_id_id'])

        # Adding model 'DirectorsGenres'
        db.create_table(u'directors_genres', (
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('prob', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('director_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['DirectorsGenres'])

        # Adding model 'MoviesGenres'
        db.create_table(u'movies_genres', (
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('movie_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'step_game', ['MoviesGenres'])

        # Adding model 'MoviesDirectors'
        db.create_table(u'movies_directors', (
            ('movie_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('director_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'step_game', ['MoviesDirectors'])

        # Adding model 'Directors'
        db.create_table(u'directors', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal(u'step_game', ['Directors'])


        # Renaming column for 'Roles.movie_id' to match new field type.
        db.rename_column(u'roles', 'movie_id_id', 'movie_id')
        # Changing field 'Roles.movie_id'
        db.alter_column(u'roles', 'movie_id', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Renaming column for 'Roles.actor_id' to match new field type.
        db.rename_column(u'roles', 'actor_id_id', 'actor_id')
        # Changing field 'Roles.actor_id'
        db.alter_column(u'roles', 'actor_id', self.gf('django.db.models.fields.IntegerField')(null=True))

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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['step_game.Movies']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'})
        }
    }

    complete_apps = ['step_game']