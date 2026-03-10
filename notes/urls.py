from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_note, name="add_note"),
    path("update/<int:id>/", views.update_note, name="update_note"),
    path("delete/<int:id>/", views.delete_note, name="delete_note"),
    path('login/', LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path("register/", views.register, name="register"),
]