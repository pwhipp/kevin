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

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = 'auth_user_user_permissions'

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

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200L)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'

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

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255L)
    migration = models.CharField(max_length=255L)
    applied = models.DateTimeField()
    class Meta:
        db_table = 'south_migrationhistory'

