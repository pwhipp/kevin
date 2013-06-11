# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Actors(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100L, blank=True)
    last_name = models.CharField(max_length=100L, blank=True)
    gender = models.CharField(max_length=1L, blank=True)
    class Meta:
        db_table = 'actors'

class Directors(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100L, blank=True)
    last_name = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'directors'

class DirectorsGenres(models.Model):
    director_id = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=100L, blank=True)
    prob = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'directors_genres'

class Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L, blank=True)
    year = models.IntegerField(null=True, blank=True)
    rank = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'movies'

class MoviesDirectors(models.Model):
    director_id = models.IntegerField(null=True, blank=True)
    movie_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'movies_directors'

class MoviesGenres(models.Model):
    movie_id = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'movies_genres'

class Roles(models.Model):
    actor_id = models.IntegerField(null=True, blank=True)
    movie_id = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'roles'

