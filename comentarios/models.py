from django.utils import timezone
from django.db import models
from django.contrib.auth.admin import User
from posts.models import Post


# Create your models here.
class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=250, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='Email')
    comentario = models.TextField(verbose_name='Comentário')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_comentario = models.DateTimeField(default=timezone.now, verbose_name='Data')
    publicado_comentario = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.nome_comentario
