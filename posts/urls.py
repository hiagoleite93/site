from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name='post_categoria'),
    path('busca/', views.PostBusca.as_view(), name='post_busca'),
    path('sobreMim/', views.SobreMim.as_view(), name='sobreMim'),
    path('posts/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    ]