from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'YourNotes'
urlpatterns = [
    path('', views.login_view, name="login_screen"),
	path('login', views.loginprocess_view, name="login_process"),
	path('register', views.register_view, name="register"),
	path('registration', views.registerprocess_view, name="register_process"),
	path('?P<username>/notelist', views.showlist_view, name="notelist"),
	path('?P<username>/addnote', views.createNote_view, name="addnote"),
	path('?P<username>/?P<title>/deletenote', views.deleteNote_view, name="deletenote"),
	path('?P<username>/?P<title>/updatenote', views.updateNote_view, name="updatenote")
]