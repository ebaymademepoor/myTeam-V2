from django.urls import path, include
from .views import user_profile, update_profile_data, update_position_pref, player_profile, rate_player_or_edit_existing, add_new_image

urlpatterns = [
    path('user_profile/<int:id>', user_profile, name="profile"),
    path('update_profile_data/<int:id>', update_profile_data, name="update_profile"),
    path('add_new_image/<int:id>', add_new_image, name="add_new_image"),
    path('update_position_pref/<int:id>', update_position_pref, name="update_position_pref"),
    path('player_profile/<int:playerid>/<int:groupid>', player_profile, name="player-profile"),
    path('rate_player/<int:player_rated>', rate_player_or_edit_existing, name="rate-player"),
]