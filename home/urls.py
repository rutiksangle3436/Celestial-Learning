from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('video/', views.video_play, name='videos'),
]