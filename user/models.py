from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)  # Importando libs bases para criação de user
from django.utils.translation import ugettext as _  # Importando tradutor de texto
from django.contrib import auth  # Importando modulo auth
from django.core.mail import send_mail  # Importando função de envio de email
from crud.settings import (
    EMAIL_HOST_USER,
    SECRET_KEY,
)  # Importando email de submissão da api
import jwt


class School(models.Model):
    name = models.CharField(max_length=200, blank=False)
    created = models.DateTimeField(
        _("created in"),
        blank=True,
        default=timezone.now,
        help_text=_("creation date"),
    )

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(
        _("name"),
        max_length=100,
        unique=True,
        help_text=_("Name given to function / role / position"),
    )
    value = models.IntegerField(
        _("value"), help_text=_("Hierarchical value of function / role / position")
    )
    created = models.DateTimeField(
        _("created in"),
        blank=True,
        default=timezone.now,
        help_text=_("role creation date"),
    )

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, email, password=None, **extra_fields
    ):  # email, password=None, **extra_fields
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def with_perm(
        self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(
        _("email address"),
        blank=True,
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
        blank=True,
        help_text=_("User registration date"),
    )
    soft_delet = models.DateTimeField(
        _("deleted"),
        blank=True,
        null=True,
        help_text=_("exclusion data the user if he has been excluded"),
    )
    is_trusty = models.DateTimeField(
        _("is trusty"), blank=True, null=True, help_text=_("date the user was verified")
    )
    cpf = models.CharField(
        _("Individual registration"),
        max_length=15,
        blank=True,
        unique=True,
        help_text=_("Individual registration"),
    )
    address = models.CharField(
        _("address"), max_length=100, blank=True, help_text=_("User address")
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text=_("user position / function / role"),
    )
    phone_number = models.CharField(
        _("phone Number"), max_length=15, blank=True, help_text=_("user's phone number")
    )
    description = models.TextField(
        _("description"), blank=True, help_text=_("brief description about the user")
    )

    processed_description = models.TextField(
        _("processed description"),
        blank=True,
        help_text=_("brief processed description about the user"),
    )

    avatar = models.ImageField(_("Avatar"), blank=True, upload_to="%Y/%m/%d/")

    uf = models.CharField(max_length=50, blank=True)

    cidade = models.CharField(max_length=200, blank=True)

    school = models.ForeignKey(School, on_delete=models.SET_NULL, blank=True, null=True)

    points = models.IntegerField(blank=True, default=0)

    classification = models.IntegerField(blank=True, default=0)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.first_name

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def save(self, *args, **kwargs):
        text = str(self.description)

        text = text.replace("\r\n", "\\n")

        self.processed_description = text

        super(User, self).save(*args, **kwargs)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_confirm_email_token(self):  # Cria um token para verificação de email
        date_hours = timezone.now()
        token = jwt.encode(
            {"id": self.id, "email": self.email, "expira": str(date_hours), "type": 1},
            SECRET_KEY,
            "HS256",
        )
        return token

    def verify_confirm_email_token(
        self, token
    ):  # Verifica token para verificação de email
        try:
            token = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        except:
            return None
        return token
