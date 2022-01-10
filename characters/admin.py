from django.contrib import admin

from characters.models import Character

# Register your models here.

class CharacterAdmin(admin.ModelAdmin):
    '''
        Admin View for Character
    '''
    list_display = ('name','alter_ego','power')
    list_filter = ('power',)
    search_fields = ('name','alter_ego')

admin.site.register(Character, CharacterAdmin)