from django.urls import path, include
from .views import match_instance, add_or_edit_a_match,update_availability_status, save_a_generated_team, rate_performance_page, add_ratings_to_db, email_availability_reminder

urlpatterns = [
    path('match_instance/<int:groupid>/<int:matchid>', match_instance, name="matches"),
    path('add_or_edit_a_match/<int:groupid>/<int:matchid>', add_or_edit_a_match, name="add-edit-match"),
    path('update_availability_status/<int:matchid>/<int:availability_table_id>', update_availability_status, name="update-status"),
    path('save_a_generated_team/<int:groupid>/<int:matchid>', save_a_generated_team, name="save-team"),
    path('rate_performance_page/<int:matchid>', rate_performance_page, name="rate-performance"),
    path('add_ratings_to_db/<int:matchid>', add_ratings_to_db, name="submit-performance-ratings"),
    path('email_availability_reminder/<int:matchid>', email_availability_reminder, name="email-availability-reminder"),
]