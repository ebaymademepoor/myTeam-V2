from django.urls import path, include
from .views import group_select, create_group, group_home, join_group

urlpatterns = [
    path('group_select/', group_select, name="group-select"),
    path('create_group/', create_group, name="create-group"),
    path('group_home/<int:id>', group_home, name="group-home"),
    path('join_group/', join_group, name="join-group"),
]