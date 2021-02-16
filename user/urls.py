from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user import views

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("reset_password/", views.reset_password, name="reset_password"),
    path("reset_password_done/", views.reset_password_done, name="reset_password_done"),
]
