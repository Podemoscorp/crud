from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("blog/", views.blog, name="blog"),
    path("post/<int:id>/", views.post, name="post"),
    path("publicar/", views.criar_post, name="publicar"),
    path("noticia/<int:id>/", views.noticia, name=""),
    path("criar/noticia/", views.criar_noticia, name="criar_noticia"),
    path("cursos/", views.cursos, name="cursos"),
    path("curso/<int:id>", views.curso, name="curso"),
    path("criar/curso/", views.criar_curso, name="criar_curso"),
    path("olimpiadas/", views.olimpiadas, name="olimpiadas"),
    path("olimpiada/<int:id>", views.olimpiada, name="olimpiada"),
    path("calendario/", views.calendario, name="calendarios"),
    path("evento/<int:id>", views.evento, name="evento"),
    path("imagens/", views.images, name="imagens"),
    path("image/<int:id>", views.image, name="image"),
    path("upload/image/", views.upload_image, name="image"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
