from django.contrib import admin

from .models import Topic, Entry


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    exclude = ('slug',)


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created', 'updated')
    list_filter = ('topic', 'created', 'updated')
