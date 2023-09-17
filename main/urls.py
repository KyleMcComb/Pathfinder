from . import views
from django.urls import path
from .chatbot import receive_message
from django.urls import path, include
from .requestFunctions.generalInfo import listOfPathways, accountInfo
from .requestFunctions.gradeInfo import gradeInfoRequest
from .requestFunctions.accountHandling import verify, signUp
from .requestFunctions.searchModules import searchModulesRequest
from .requestFunctions.backupHandling import listLocalBackupFiles, listCloudBackupFiles, restoreBackup, rollbackBackup, deleteBackup

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('receive_message/', views.receive_message, name='receive_message'),
    path('Settings/', views.settings, name='settings'),
    path('GradeDashboard/', views.gradeDashboard, name='GradeDashboard'),
    path('ModuleInformation/', views.moduleInformation, name='ModuleInformation'),
    path('receive_message/', receive_message, name='receive_message'),
    path('verify/', verify, name='verify'),
    path('gradeInfo/', gradeInfoRequest, name='gradeInfo'),
    path('listOfPathways/', listOfPathways, name='listOfPathways'),
    path('signUp/', signUp, name='signUp'),
    path('accountInfo/', accountInfo, name='accountInfo'),
    path('searchModules/', searchModulesRequest, name='searchModules'),
    path('listLocalBackupFiles/', listLocalBackupFiles, name='listLocalBackupFiles'),
    path('listCloudBackupFiles/', listCloudBackupFiles, name='listCloudBackupFiles'),
    path('restoreBackup/', restoreBackup, name='restoreBackup'),
    path('rollbackBackup/', rollbackBackup, name='rollbackBackup'),
    path('deleteBackup/', deleteBackup, name='deleteBackup')
]