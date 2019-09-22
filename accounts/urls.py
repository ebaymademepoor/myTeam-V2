from django.urls import path
from accounts.views import index, logout, get_started, login, registration, about_us, contact_us

urlpatterns = [
    path('logout/', logout, name="logout"),
    path('get-started/', get_started, name="get-started"),
    path('login/', login, name="login"),
    path('register/', registration, name="register"),
    path('about-us', about_us, name="about-us"),
    path('contact-us', contact_us, name="contact-us"),
]
