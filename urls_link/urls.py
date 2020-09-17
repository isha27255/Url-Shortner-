from django.urls import path
from django.conf.urls import url
from .views import *
from urls_link import views

urlpatterns = [
    path("", index, name="index"),
    path("<str:shorted_link>", get_shorten_link, name="get_shorten_link"),

 ]