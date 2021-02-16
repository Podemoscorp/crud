from django.contrib import admin
from core.models import Noticia, Post, Curso, Matricula, Certificado, Evento, Image


class AdminNoticias(admin.ModelAdmin):
    list_display = ("id", "title", "poster", "abstract", "posted_in")
    list_display_links = ("id", "title", "poster", "abstract", "posted_in")
    search_fields = ("id", "title", "poster", "abstract", "posted_in", "content")
    list_per_page = 20


class AdminPosts(admin.ModelAdmin):
    list_display = ("id", "title", "poster", "posted_in")
    list_display_links = ("id", "title", "poster", "posted_in")
    search_fields = ("id", "title", "poster", "posted_in", "content")
    list_per_page = 20


class AdminCursos(admin.ModelAdmin):
    list_display = ("id", "name", "created", "teacher", "theme")
    list_display_links = ("id", "name", "created", "teacher", "theme")
    search_fields = ("id", "name", "created", "teacher", "theme", "description")
    list_per_page = 20


class AdminMatriculas(admin.ModelAdmin):
    list_display = ("id", "student", "course", "created", "finished")
    list_display_links = ("id", "student", "course", "created", "finished")
    search_fields = ("id", "student", "course", "created", "finished")
    list_per_page = 20


class AdminCertificados(admin.ModelAdmin):
    list_display = ("id", "title", "teacher", "student", "course", "created")
    list_display_links = ("id", "title", "teacher", "student", "course", "created")
    search_fields = (
        "id",
        "title",
        "teacher",
        "student",
        "course",
        "created" "description",
    )
    list_per_page = 20


class AdminEventos(admin.ModelAdmin):
    list_display = ("id", "starts_at", "ends_in", "title", "created")
    list_display_links = ("id", "starts_at", "ends_in", "title", "created")
    search_fields = ("id", "starts_at", "ends_in", "title", "created", "description")
    list_per_page = 20


class AdminImages(admin.ModelAdmin):
    list_display = ()
    list_display_links = ()
    search_fields = ()
    list_per_page = 20


admin.site.register(Noticia, AdminNoticias)
admin.site.register(Post, AdminPosts)
admin.site.register(Curso, AdminCursos)
admin.site.register(Matricula, AdminMatriculas)
admin.site.register(Certificado, AdminCertificados)
admin.site.register(Evento, AdminEventos)
admin.site.register(Image, AdminImages)
