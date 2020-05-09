from django.contrib import admin
from django.urls import path
from Data import views

urlpatterns = [
    path('', views.index),
    path('classification', views.Classification),
    path('knn-classification', views.KNN_Classification),
    path('download', views.KNN_Classify),
]
