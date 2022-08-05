from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.AuthorAPI.as_view(), name='AuthorAPI'),
]