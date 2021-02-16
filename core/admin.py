from django.contrib import admin
from core.models import Noticias, Posts, Curso, Matricula, Certificado, Evento


class AdminNoticias(admin.ModelAdmin):
    list_display = ("id", "titulo", "postador", "resumo", "postado_em")
    list_display_links = ("id", "titulo", "postador", "resumo", "postado_em")
    search_fields = ("id", "titulo", "postador", "resumo", "conteudo")
    list_per_page = 20


class AdminPosts(admin.ModelAdmin):
    list_display = ("id", "titulo", "postador", "postado_em")
    list_display_links = ("id", "titulo", "postador", "postado_em")
    search_fields = ("id", "titulo", "postador", "postado_em", "conteudo")
    list_per_page = 20


class AdminCursos(admin.ModelAdmin):
    list_display = ("id", "nome", "criado_em", "professor", "tema")
    list_display_links = ("id", "nome", "criado_em", "professor", "tema")
    search_fields = ("id", "nome", "descricao", "criado_em", "professor", "tema")
    list_per_page = 20


class AdminMatriculas(admin.ModelAdmin):
    list_display = ("id", "aluno", "curso", "datetime")
    list_display_links = ("id", "aluno", "curso", "datetime")
    search_fields = ("id", "aluno", "curso", "datetime")
    list_per_page = 20


class AdminCertificados(admin.ModelAdmin):
    list_display = ("id", "titulo", "professor", "aluno", "curso", "criado_em")
    list_display_links = ("id", "titulo", "professor", "aluno", "curso", "criado_em")
    search_fields = (
        "id",
        "titulo",
        "professor",
        "aluno",
        "curso",
        "criado_em",
        "descricao",
    )
    list_per_page = 20


class AdminEventos(admin.ModelAdmin):
    list_display = ("id", "comeca_em", "termina_em", "titulo", "criado_em")
    list_display_links = ("id", "comeca_em", "termina_em", "titulo", "criado_em")
    search_fields = (
        "id",
        "comeca_em",
        "termina_em",
        "titulo",
        "descricao",
        "criado_em",
    )
    list_per_page = 20


admin.site.register(Noticias, AdminNoticias)
admin.site.register(Posts, AdminPosts)
admin.site.register(Curso, AdminCursos)
admin.site.register(Matricula, AdminMatriculas)
admin.site.register(Certificado, AdminCertificados)
admin.site.register(Evento, AdminEventos)
