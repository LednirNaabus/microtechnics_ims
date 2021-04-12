from django.urls import path
from . import views

"""
-- first url: login.html
---- once logged in -> views.home
"""

urlpatterns = [
    path('', views.login),
    path('forgot-pass/', views.forgotpass),
    path('recover-pass/', views.newpass),
    path('home/', views.home),
]
