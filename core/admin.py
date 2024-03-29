from django.contrib import admin
from core.models import (
    New,
    Post,
    Course,
    Registration,
    Certificate,
    Event,
    Image,
    CourseType,
    Subject,
    SubjectNew,
    SubjectPost,
    Challenge,
    Olimpimat,
)


class AdminNews(admin.ModelAdmin):
    list_display = ("id", "title", "poster", "abstract", "posted_in")
    list_display_links = ("id", "title", "poster", "abstract", "posted_in")
    search_fields = ("id", "title", "poster", "abstract", "posted_in", "content")
    list_per_page = 20


class AdminPosts(admin.ModelAdmin):
    list_display = ("id", "title", "poster", "posted_in")
    list_display_links = ("id", "title", "poster", "posted_in")
    search_fields = ("id", "title", "poster", "posted_in", "content")
    list_per_page = 20


class AdminCourses(admin.ModelAdmin):
    list_display = ("id", "name", "created", "teacher", "theme")
    list_display_links = ("id", "name", "created", "teacher", "theme")
    search_fields = ("id", "name", "created", "teacher", "theme", "description")
    list_per_page = 20


class AdminRegistrations(admin.ModelAdmin):
    list_display = ("id", "student", "course", "created", "finished")
    list_display_links = ("id", "student", "course", "created", "finished")
    search_fields = ("id", "student", "course", "created", "finished")
    list_per_page = 20


class AdminCertificates(admin.ModelAdmin):
    list_display = ("id", "title", "teacher", "student", "course", "created")
    list_display_links = ("id", "title", "teacher", "student", "course", "created")
    search_fields = (
        "id",
        "title",
        "teacher",
        "student",
        "course",
        "created",
        "description",
    )
    list_per_page = 20


class AdminEvents(admin.ModelAdmin):
    list_display = ("id", "starts_at", "ends_in", "title", "created")
    list_display_links = ("id", "starts_at", "ends_in", "title", "created")
    search_fields = ("id", "starts_at", "ends_in", "title", "created", "description")
    list_per_page = 20


class AdminImages(admin.ModelAdmin):
    list_display = ("id", "name", "upload_in")
    list_display_links = ("id", "name", "upload_in")
    search_fields = ("id", "name", "upload_in", "image")
    list_per_page = 20


class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created")
    list_display_links = ("id", "name", "created")
    search_fields = ("id", "name", "created")
    list_per_page = 20


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created")
    list_display_links = ("id", "name", "created")
    search_fields = ("id", "name", "created")
    list_per_page = 20


class SubjectAdminNew(admin.ModelAdmin):
    list_display = ("id", "new", "created_in", "subject")
    list_display_links = ("id", "new", "created_in", "subject")
    search_fields = ("id", "new", "created_in", "subject")
    list_per_page = 20


class SubjectAdminPost(admin.ModelAdmin):
    list_display = ("id", "post", "created_in", "subject")
    list_display_links = ("id", "post", "created_in", "subject")
    search_fields = ("id", "post", "created_in", "subject")
    list_per_page = 20


class AdminOlimpiada(admin.ModelAdmin):
    list_display = ("id", "nome", "criado_em")
    list_display_links = ("id", "nome", "criado_em")
    search_fields = ("id", "nome", "criado_em", "descricao")
    list_per_page = 20


class AdminChallenge(admin.ModelAdmin):
    list_display = ("id", "data_de_inicio", "data_de_termino", "criado_em")
    list_display_links = ("id", "data_de_inicio", "data_de_termino", "criado_em")
    search_fields = (
        "id",
        "descricao",
        "data_de_inicio",
        "data_de_termino",
        "criado_em",
    )
    list_per_page = 20


admin.site.register(New, AdminNews)
admin.site.register(Post, AdminPosts)
admin.site.register(Course, AdminCourses)
admin.site.register(Registration, AdminRegistrations)
admin.site.register(Certificate, AdminCertificates)
admin.site.register(Event, AdminEvents)
admin.site.register(Image, AdminImages)
admin.site.register(CourseType, CourseTypeAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectNew, SubjectAdminNew)
admin.site.register(SubjectPost, SubjectAdminPost)
admin.site.register(Olimpimat, AdminOlimpiada)
admin.site.register(Challenge, AdminChallenge)
