from django.contrib import admin


from apps.base import models
# Register your models here.

class ClientsAll(admin.TabularInline):
    model = models.ClientsInline
    extra = 1

class ClientsFilterAdmin(admin.ModelAdmin):
    list_filter = ('description',)
    list_display = ('description',)
    search_fields = ('description', )
    inlines = [ClientsAll]

class NewsAll(admin.TabularInline):
    model = models.NewsInline
    extra = 1

class NewsFilterAdmin(admin.ModelAdmin):
    list_filter = ('main_title',)
    list_display = ('main_title',)
    search_fields = ('main_title', )
    inlines = [NewsAll]

admin.site.register(models.News, NewsFilterAdmin)
admin.site.register(models.Clients, ClientsFilterAdmin)
admin.site.register(models.Settings)
admin.site.register(models.Slide)
admin.site.register(models.Collection)
admin.site.register(models.NewArrival)
admin.site.register(models.Card)