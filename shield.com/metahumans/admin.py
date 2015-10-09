from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from metahumans.models import Power, Team, SuperHero, Capabilities

class PowerAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'description')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['slug', 'name', 'description']

admin.site.register(Power, PowerAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'active', 'num_members')
    list_filter = ('active', )
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['slug', 'name', 'headquarters', 'description']

    def team_name(self, obj):
        if obj.active:
            return format_html(obj.name)
        else:
            return format_html(
                '<span style="text-decoration: line-through;">'
                '{}'
                '</span>'.format(obj.name))

    team_name.allow_tags = True



admin.site.register(Team, TeamAdmin)

class CapabilitiesInline(admin.TabularInline):
    model = Capabilities

class SuperHeroAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'active', 'list_of_powers', 'has_photo')
    list_filter = ('active', 'team__name')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['slug', 'name', 'headquarters', 'description']
    inlines = [
        CapabilitiesInline
        ]

admin.site.register(SuperHero, SuperHeroAdmin)
