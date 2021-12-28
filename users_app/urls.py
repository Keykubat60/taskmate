from django.urls import path
from users_app import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name = 'login.html'), name= 'login'),
path('logout', auth_views.LogoutView.as_view(template_name = 'logout.html'), name= 'logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)