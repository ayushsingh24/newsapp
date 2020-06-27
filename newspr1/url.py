from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name="home"),
    path('other_language.html', views.other_language ,name="news in hindi"),

]