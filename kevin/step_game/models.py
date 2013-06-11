"""This is the supplied model for the demo converted directly into an
ORM (with no relations to speak of ;). It can be substantially
improved by correctly defining the relationships. Until that is done,
the admin support will be patchy because there are tables with no key
fields etc."""
from __future__ import unicode_literals

from django.db import models

class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100L, blank=True)
    last_name = models.CharField(max_length=100L, blank=True)
    gender = models.CharField(max_length=1L, blank=True)
    class Meta:
        db_table = 'actors'
    def __unicode__(self):
        return "{0}, {1}".format(self.last_name, self.first_name)
    
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L, blank=True)
    year = models.IntegerField(null=True, blank=True)
    rank = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'movies'
    def __unicode__(self):
        return "{0} ({1})".format(self.name, self.year)

class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    actor = models.ForeignKey(Actor)
    movie = models.ForeignKey(Movie)
    role = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'roles'
    def __unicode__(self):
        return "{0}-{1}-{2}".format(self.actor, self.movie, self.role)

