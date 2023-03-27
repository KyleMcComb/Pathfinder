from django.urls import path
from . import views
from .chatbot import receive_message

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    #path('receive_message/', receive_message, name='receive_message'),
    path('receive_message/', views.receive_message, name='receive_message'),
]