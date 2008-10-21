from pholius.core import models
from django.contrib import admin

class ContentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Content header',  {'fields': ['title', 'slug']}),
        ('Content body',    {'fields': ['body']}),
        ('Content miscs',   {'fields': ['author', 'taxonomy']}),
    ]

admin.site.register(models.Content, ContentAdmin)
admin.site.register(models.Taxonomy)

