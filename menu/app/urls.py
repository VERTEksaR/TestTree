from django.urls import path

from app.views import draw_menu


urlpatterns = [
    path('<str:name_menu>/', draw_menu),
]
