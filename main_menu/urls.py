from django.urls import path

from .apps import MainMenuConfig
from .views import IndexPageView

app_name = MainMenuConfig.name

urlpatterns = [
    path("", IndexPageView.as_view(), name="main_menu")
]
