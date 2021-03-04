from django.urls import path
from user import views

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("reset_password/", views.reset_password, name="reset_password"),
    path("reset_password/done/", views.reset_password_done, name="reset_password_done"),
    path(
        "reset_password/confirm/<str:token>/",
        views.reset_password_confirm,
        name="reset_password_confirm",
    ),
    path("perfil/<int:id>/", views.perfil, name="perfil"),
    path("editar/perfil/", views.editar_perfil, name="editar_perfil"),
    path("confirmar/email/<str:token>/", views.confirma_email, name="confirmar_email"),
    path("cadastro/done/", views.cadastro_done, name="cadastro_done"),
]
