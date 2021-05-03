from django.db import models
from django.utils import timezone
from user.models import User
from django.utils.translation import ugettext as _
import PIL
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class Subject(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(
        _("created in"),
        blank=True,
        default=timezone.now,
        help_text=_("Subject creation date"),
    )

    def __str__(self):
        return self.name


class New(models.Model):

    visibilities = (
        ("A", "Privado"),
        ("B", "Publico"),
        ("C", "Comunidade"),
    )

    title = models.CharField(
        _("Title"), max_length=100, help_text=_("title of the news")
    )
    abstract = models.TextField(_("Abstract"), help_text=_("news summary"))
    processed_abstract = models.TextField(
        _("processed Abstract"),
        help_text=_("news processed summary"),
        blank=True,
        default="",
    )
    content = models.TextField(_("Content"), help_text=_("news content"))
    processed_content = models.TextField(
        _("Processed Content"),
        help_text=_("news processed content"),
        blank=True,
        default="",
    )
    image = models.ImageField(
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
    visibility = models.CharField(
        _("visibility "),
        max_length=2,
        choices=visibilities,
        help_text=_("visibility of the news"),
    )
    views = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title

    def save(self):
        text = str(self.content)
        text = text.replace("\r\n", "\\n ")

        self.processed_content = text

        text_abstract = str(self.abstract)
        text_abstract = text_abstract.replace("\r\n", "\\n ")

        self.processed_abstract = text_abstract

        img = None

        try:
            img = PIL.Image.open(self.image).convert("RGB")
        except:
            img = Image.open(self.image).convert("RGB")

        buffer = BytesIO()

        # Resize/modify the image
        img = img.resize((900, 506))

        # after modifications, save it to the output
        img.save(buffer, format="JPEG", quality=100)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(
            buffer,
            None,
            "%s.jpg" % self.image.name.split(".")[0],
            "image/jpeg",
            len(buffer.getbuffer()),
            None,
        )

        super(New, self).save()


class Post(models.Model):
    visibilities = (
        ("A", "Privado"),
        ("B", "Publico"),
        ("C", "Comunidade"),
    )

    title = models.CharField(_("Title"), max_length=100, help_text=_("post title"))
    content = models.TextField(_("Content"), help_text=_("post content"))
    processed_content = models.TextField(
        _("Processed Content"),
        help_text=_("post processed content"),
        blank=True,
        default="",
    )
    image = models.ImageField(
        _("Image"),
        upload_to="%Y/%m/%d/",
        blank=False,
        help_text=_("post cover image"),
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

    visibility = models.CharField(
        _("visibility "),
        max_length=2,
        choices=visibilities,
        help_text=_("publication visibility"),
    )
    views = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title

    def save(self):
        text = str(self.content)
        text = text.replace("\r\n", "\\n ")

        self.processed_content = text

        img = None
        try:
            img = PIL.Image.open(self.image).convert("RGB")
        except:
            img = Image.open(self.image).convert("RGB")

        buffer = BytesIO()

        # Resize/modify the image
        img = img.resize((900, 506))

        # after modifications, save it to the output
        img.save(buffer, format="JPEG", quality=100)

        # change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(
            buffer,
            None,
            "%s.jpg" % self.image.name.split(".")[0],
            "image/jpeg",
            len(buffer.getbuffer()),
            None,
        )

        super(Post, self).save()


class SubjectNew(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_in = models.DateTimeField(default=timezone.now, blank=True)


class SubjectPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_in = models.DateTimeField(default=timezone.now, blank=True)


class CourseType(models.Model):
    image = models.FileField(
        _("Image"),
        upload_to="%Y/%m/%d/",
        blank=True,
        help_text=_("Course Type cover image"),
    )
    name = models.CharField(_("Name"), max_length=200, help_text=_("course type name"))
    created = models.DateTimeField(
        _("Created in"),
        default=timezone.now,
        blank=True,
        help_text=_("Course Type creation date"),
    )

    def __str__(self):
        return self.name


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
    type = models.ForeignKey(
        CourseType, on_delete=models.SET_NULL, null=True, blank=True
    )

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
    tipos = (
        ("A", "Olimpiada"),
        ("B", "Evento"),
        ("C", "Feira de ciências"),
    )

    regioes = (
        ("A", "Nacional"),
        ("B", "Internacional"),
    )

    starts_at = models.DateTimeField(_("Starts in"), help_text=_("Event start date"))
    ends_in = models.DateTimeField(_("Ends in"), help_text=_("End date of the event"))
    title = models.CharField(
        _("Title"), max_length=100, help_text=_("title of the event")
    )
    description = models.TextField(
        _("Description"), help_text=_("Event description or summary")
    )
    tipo = models.CharField(max_length=2, choices=tipos)
    regiao = models.CharField(max_length=2, choices=regioes)
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

    uploader = models.ForeignKey(
        User, blank=True, null=True, default=1, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name


class Olimpimat(models.Model):
    nome = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to="desafio/%Y/%m/%d/")
    descricao = models.TextField()
    processed_descricao = models.TextField(blank=True)
    regulamento = models.FileField(upload_to="desafio/%Y/%m/%d/")
    cronograma = models.FileField(upload_to="desafio/%Y/%m/%d/")
    criado_em = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.nome

    def save(self):
        text = str(self.descricao)
        text = text.replace("\r\n", "\\n ")

        self.processed_descricao = text

        super(Olimpimat, self).save()


class Challenge(models.Model):
    status_choices = (("Aberto", "A"), ("Encerrado", "B"))
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    data_de_inicio = models.DateField()
    data_de_termino = models.DateField()
    prova = models.FileField(blank=True, upload_to="desafio/%Y/%m/%d/")
    gabarito = models.FileField(blank=True, upload_to="desafio/%Y/%m/%d/")
    url_cadastro = models.URLField(blank=True)
    url_prova = models.URLField()
    resultado = models.FileField(blank=True, upload_to="desafio/%Y/%m/%d/")
    criado_em = models.DateTimeField(blank=True, default=timezone.now)
    edicao_olimpiada = models.ForeignKey(
        Olimpimat, on_delete=models.CASCADE, null=True, blank=True
    )
    status = models.CharField(max_length=50, blank=True, choices=status_choices)

    def __str__(self):
        return self.nome

    def get_status(self):
        if self.status == "Aberto":
            return f"Aberto até {self.data_de_termino}"
        else:
            return self.status
