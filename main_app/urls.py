from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('designs/', views.Designs_List.as_view(), name="design_list"),
]