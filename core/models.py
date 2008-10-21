from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Taxonomy(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=32)
    type = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    class Meta:
	    verbose_name_plural = 'taxonomies'

    def __unicode__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=80, unique_for_date='created')
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    taxonomy = models.ManyToManyField(Taxonomy, blank=True)
    #response_count = models.SmallIntegerField(maxlength=4)
    #allow_comments = models.BooleanField()
    #allow_pings = models.BooleanField()

    def __unicode__(self):
        return self.title    
