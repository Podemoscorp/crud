from django.db import models
from django.utils import timezone
from user.models import User
from django.utils.translation import ugettext as _


class Noticia(models.Model):
    title = models.CharField(_("Title"), max_length=100, help_text=_(""))
    abstract = models.TextField(_("Abstract"), help_text=_(""))
    content = models.TextField(_("Content"), help_text=_(""))
    image = models.FileField(
        _("Image"), upload_to="%Y/%m/%d/", blank=True, help_text=_("")
    )
    posted_in = models.DateTimeField(
        _("Posted in"), default=timezone.now, blank=True, help_text=_("")
    )
    poster = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_(""))

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=100, help_text=_(""))
    content = models.TextField(_("Content"), help_text=_(""))
    image = models.FileField(
        _("Image"), upload_to="%Y/%m/%d/", blank=True, help_text=_("")
    )
    posted_in = models.DateTimeField(
        _("Posted in"), default=timezone.now, blank=True, help_text=_("")
    )
    poster = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_(""))

    def __str__(self):
        return self.title


class Curso(models.Model):
    name = models.CharField(_("Name"), max_length=200, help_text=_(""))
    description = models.TextField(_("Description"), help_text=_(""))
    image = models.FileField(
        _("Image"), upload_to="%Y/%m/%d/", blank=True, help_text=_("")
    )
    created = models.DateTimeField(
        _("Created in"), default=timezone.now, blank=True, help_text=_("")
    )
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_(""))
    theme = models.CharField(_("Theme"), max_length=30, help_text=_(""))

    def __str__(self):
        return self.name


class Matricula(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_(""))
    course = models.ForeignKey(Curso, on_delete=models.CASCADE, help_text=_(""))
    created = models.DateTimeField(
        _("Created in"), default=timezone.now, blank=True, help_text=_("")
    )
    finished = models.DateTimeField(
        _("Finished"), blank=True, null=True, help_text=_("")
    )


class Certificado(models.Model):
    title = models.CharField(_("Title"), max_length=100, help_text=_(""))
    description = models.TextField(_("Description"), blank=True, help_text=_(""))
    file = models.FileField(
        _("File"), upload_to="%Y/%m/%d/", blank=True, help_text=_("")
    )
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Professor", help_text=_("")
    )
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Alunos", help_text=_("")
    )
    course = models.ForeignKey(Curso, on_delete=models.CASCADE, help_text=_(""))
    created = models.DateTimeField(
        _("Created"), default=timezone.now, blank=True, help_text=_("")
    )

    def __str__(self):
        return self.title


class Evento(models.Model):
    starts_at = models.DateTimeField(_("Starts in"), help_text=_(""))
    ends_in = models.DateTimeField(_("Ends in"), help_text=_(""))
    title = models.CharField(_("Title"), max_length=100, help_text=_(""))
    description = models.TextField(_("Description"), help_text=_(""))
    created = models.DateTimeField(
        _("Created"), default=timezone.now, blank=True, help_text=_("")
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.FileField(_("Image"), help_text=_(""))
    name = models.CharField(_("Name"), max_length=100, help_text=_(""))
    upload_in = models.DateTimeField(
        _("Upload in"), blank=True, default=timezone.now, help_text=_("")
    )
