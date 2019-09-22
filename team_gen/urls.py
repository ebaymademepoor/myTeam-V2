from django.urls import path, include
from .views import team_gen_settings

urlpatterns = [
    path('team_gen_settings/<int:matchid>', team_gen_settings, name="team-gen-settings"),
]