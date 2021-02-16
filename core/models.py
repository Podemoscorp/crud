from django.db import models
from django.utils import timezone
from user.models import User
from django.utils.translation import ugettext as _


class Noticia(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    abstract = models.TextField(_("Abstract"))
    content = models.TextField(_("Content"))
    image = models.FileField(_("Image"), upload_to="%Y/%m/%d/", blank=True)
    posted_in = models.DateTimeField(_("Posted in"), default=timezone.now, blank=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    content = models.TextField(_("Content"))
    image = models.FileField(_("Image"), upload_to="%Y/%m/%d/", blank=True)
    posted_in = models.DateTimeField(_("Posted in"), default=timezone.now, blank=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Curso(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    description = models.TextField(_("Description"))
    image = models.FileField(_("Image"), upload_to="%Y/%m/%d/", blank=True)
    created = models.DateTimeField(_("Created in"), default=timezone.now, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.CharField(_("Theme"), max_length=30)

    def __str__(self):
        return self.name


class Matricula(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)
    created = models.DateTimeField(_("Created in"), default=timezone.now, blank=True)
    finished = models.DateTimeField(_("Finished"), blank=True, null=True)


class Certificado(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"), blank=True)
    file = models.FileField(_("File"), upload_to="%Y/%m/%d/", blank=True)
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Professor"
    )
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Alunos"
    )
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)
    created = models.DateTimeField(_("Created"), default=timezone.now, blank=True)

    def __str__(self):
        return self.title


class Evento(models.Model):
    starts_at = models.DateTimeField(_("Starts in"))
    ends_in = models.DateTimeField(_("Ends in"))
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"))
    created = models.DateTimeField(_("Created"), default=timezone.now, blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.FileField(_("Image"))
    name = models.CharField(_("Name"), max_length=100)
    upload_in = models.DateTimeField(_("Upload in"), blank=True, default=timezone.now)
