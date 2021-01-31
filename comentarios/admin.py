from django.contrib import admin
from .models import Comentario


# Register your models here.
class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_comentario', 'email_comentario', 'post_comentario',
                    'data_comentario', 'publicado_comentario',)
    list_editable = ('publicado_comentario',)
    list_display_links = ('id', 'nome_comentario', 'email_comentario',)


admin.site.register(Comentario, ComentariosAdmin)