from django.urls import path
from . import views
from .chatbot import receive_message
from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('receive_message/', views.receive_message, name='receive_message'),
    path('Settings/', views.settings, name='settings'),
    path('GradeDashboard/', views.gradeDashboard, name='GradeDashboard'),
    path('ModuleInformation/', views.moduleInformation, name='ModuleInformation'),
    path('receive_message/', receive_message, name='receive_message'),
    path('verify/', views.verify, name='verify'),
    path('gradeInfo/', views.gradeInfo, name='gradeInfo'),
    path('listOfPathways/', views.listOfPathways, name='listOfPathways'),
    path('signUp/', views.signUp, name='signUp'),
    path('accountInfo/', views.accountInfo, name='accountInfo'),
    path('searchModules/', views.searchModules, name='searchModules'),
    path('listLocalBackupFiles/', views.listLocalBackupFiles, name='listLocalBackupFiles'),
    path('listCloudBackupFiles/', views.listCloudBackupFiles, name='listCloudBackupFiles'),
    path('restoreBackup/', views.restoreBackup, name='restoreBackup'),
    path('rollbackBackup/', views.rollbackBackup, name='rollbackBackup'),
    path('deleteBackup/', views.deleteBackup, name='deleteBackup')
]