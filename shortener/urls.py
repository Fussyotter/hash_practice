from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_url>/', views.redirect_view, name='redirect'),
]
