from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_test, name='test'),
    path('/dijkstra', views.dijkstra, name="dijkstra")
]