from django.contrib import admin

from apps.secondary import models
# Register your models here.

class TeamAll(admin.TabularInline):
    model = models.TeamInline
    extra = 1

class TeamFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', 'main_description')
    list_display = ('title', "main_description")
    search_fields = ('title', )
    inlines = [TeamAll]



admin.site.register(models.Team, TeamFilterAdmin )
admin.site.register(models.About)
admin.site.register(models.Faq)


