from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("login.html", views.login, name="login"),
    path("sign_up.html", views.signup, name="signup"),
    path("dashboard2.html", views.dashboard, name="dashboard"),
    path("dashboard4.html", views.dashboard4, name="dashboard4"),
    path("dashboard5.html", views.dashboard5, name="dashboard5"),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
