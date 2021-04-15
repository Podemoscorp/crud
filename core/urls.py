from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("blog/", views.blog, name="blog"),
    path("noticias/", views.noticias, name="noticias"),
    path("post/<int:id>/", views.post, name="post"),
    path("publicar/", views.criar_post, name="publicar"),
    path("noticia/<int:id>/", views.noticia, name="noticia"),
    path("criar/noticia/", views.criar_noticia, name="criar_noticia"),
    path("cursos/", views.cursos, name="cursos"),
    path("curso/<int:id>", views.curso, name="curso"),
    path("criar/curso/", views.criar_curso, name="criar_curso"),
    path("olimpiadas/", views.olimpiadas, name="olimpiadas"),
    path("olimpiada/<int:id>", views.olimpiada, name="olimpiada"),
    path("calendario/", views.calendario, name="calendario"),
    path("evento/<int:id>", views.evento, name="evento"),
    path("imagens/", views.images, name="imagens"),
    path("imagem/<int:id>", views.image, name="image"),
    path("upload/imagem/", views.upload_image, name="upload_image"),
    path("ranking/", views.ranking, name="ranking"),
    path("updater/", views.update_ranking),
    path("olimpimat/", views.olimpimat, name="olimpimat"),
    path("desafio/<int:id>/", views.challenge, name="challenge"),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
