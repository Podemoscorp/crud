from django.db import models
from django.utils import timezone
from user.models import User
from django.utils.translation import ugettext as _


class New(models.Model):
    title = models.CharField(
        _("Title"), max_length=100, help_text=_("title of the news")
    )
    abstract = models.TextField(_("Abstract"), help_text=_("news summary"))
    content = models.TextField(_("Content"), help_text=_("news content"))
    image = models.FileField(
        _("Image"), upload_to="%Y/%m/%d/", blank=True, help_text=_("news cover image")
    )
    posted_in = models.DateTimeField(
        _("Posted in"),
        default=timezone.now,
        blank=True,
        help_text=_("news posting date"),
    )
    poster = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text=_("news editor")
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=100, help_text=_("post title"))
    content = models.TextField(_("Content"), help_text=_("post content"))
    image = models.FileField(
        _("Image"), upload_to="%Y/%m/%d/", blank=True, help_text=_("post cover image")
    )
    posted_in = models.DateTimeField(
        _("Posted in"),
        default=timezone.now,
        blank=True,
        help_text=_("post publication date"),
    )
    poster = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text=_("post editor")
    )

    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(_("Name"), max_length=200, help_text=_("course name"))
    description = models.TextField(_("Description"), help_text=_("Course description"))
    image = models.FileField(
        _("Image"), upload_to="%Y/%m/%d/", blank=True, help_text=_("Course cover image")
    )
    created = models.DateTimeField(
        _("Created in"),
        default=timezone.now,
        blank=True,
        help_text=_("Course creation date"),
    )
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text=_("Course teacher")
    )
    theme = models.CharField(_("Theme"), max_length=30, help_text=_("course theme"))

    def __str__(self):
        return self.name


class Registration(models.Model):
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text=_("enrollment student")
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, help_text=_("enrollment course")
    )
    created = models.DateTimeField(
        _("Created in"),
        default=timezone.now,
        blank=True,
        help_text=_("registration creation date"),
    )
    finished = models.DateTimeField(
        _("Finished"),
        blank=True,
        null=True,
        help_text=_("end date of the student's enrollment course"),
    )


class Certificate(models.Model):
    title = models.CharField(
        _("Title"), max_length=100, help_text=_("certificate title")
    )
    description = models.TextField(
        _("Description"), blank=True, help_text=_("certificate description")
    )
    file = models.FileField(
        _("File"),
        upload_to="%Y/%m/%d/",
        blank=True,
        help_text=_("file with the certificate"),
    )
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="Professor",
        help_text=_(
            "teacher responsible for sending the certificate to the system / issuing the certificate"
        ),
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="Alunos",
        help_text=_("student who will receive the certificate"),
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, help_text=_("certificate course")
    )
    created = models.DateTimeField(
        _("Created"),
        default=timezone.now,
        blank=True,
        help_text=_("certificate creation date"),
    )

    referring_registration = models.ForeignKey(
        Registration,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("Enrollment contained in the certificate"),
    )

    def __str__(self):
        return self.title


class Event(models.Model):
    starts_at = models.DateTimeField(_("Starts in"), help_text=_("Event start date"))
    ends_in = models.DateTimeField(_("Ends in"), help_text=_("End date of the event"))
    title = models.CharField(
        _("Title"), max_length=100, help_text=_("title of the event")
    )
    description = models.TextField(
        _("Description"), help_text=_("Event description or summary")
    )
    created = models.DateTimeField(
        _("Created"),
        default=timezone.now,
        blank=True,
        help_text=_("creation date of the event in the system"),
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.FileField(
        _("Image"), upload_to="%Y/%m/%d/", help_text=_("Image url and path")
    )
    name = models.CharField(
        _("Name"), max_length=100, help_text=_("Image name"), blank=True
    )
    upload_in = models.DateTimeField(
        _("Upload in"),
        blank=True,
        default=timezone.now,
        help_text=_("image upload date"),
    )

    def __str__(self):
        return self.name
