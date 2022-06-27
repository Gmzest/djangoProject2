from django.contrib import admin
from.models import *

admin.site.register(Type)
admin.site.register(Format)
admin.site.register(Classifier)
admin.site.register(Technology)
admin.site.register(Language)

class BookAdmin(admin.ModelAdmin):
    list_display = ('id_doc', 'short_name', 'autor', 'rel_date_doc')
    list_display_links = ('id_doc', 'short_name')
    search_fields = ('short_name', 'autor')
    list_filter = ('rel_date_doc', 'autor', 'type_doc', 'language', 'format_doc', 'classifier_doc', 'technology_doc')
    #list_editable = ('autor',)

admin.site.register(Book, BookAdmin)