from django.contrib import admin

# Register your models here.

from metahumans.models import Power, Team, SuperHero, Capabilities

class PowerAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'description')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['slug', 'name', 'description']

admin.site.register(Power, PowerAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'active',)
    list_filter = ('active', )
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['slug', 'name', 'headquarters', 'description']

admin.site.register(Team, TeamAdmin)

class CapabilitiesInline(admin.TabularInline):
    model = Capabilities

class SuperHeroAdmin(admin.ModelAdmin):
    list_display = ('slug', '__str__', 'active', 'list_of_powers')
    list_filter = ('active', 'team__name')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['slug', 'name', 'headquarters', 'description']
    inlines = [
        CapabilitiesInline
        ]

admin.site.register(SuperHero, SuperHeroAdmin)
