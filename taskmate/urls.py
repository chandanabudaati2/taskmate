from django.contrib import admin
from django.urls import path, include
from todolist_app import views as todolist_app_views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("task/", include("todolist_app.urls")),
    path("account/", include("users_app.urls")),
    # Added trailing slashes for consistency
    path("contact/", todolist_app_views.contact, name="contact"),
    path("about-us/", todolist_app_views.about, name="about"),
    path("", todolist_app_views.index, name="index"), # Root path usually doesn't have a trailing slash
]
