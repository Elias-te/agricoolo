from django.urls import path
from . import views



urlpatterns = [
    path('analyze/', views.analyze_query, name='analyze_query'),
    
   
    path('my-analyses/', views.get_user_analyses, name='get_user_analyses'),
]
