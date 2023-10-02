from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for combine_and_save_video view
    path('combine_video/', views.combine_and_save_video, name='combine_and_save_video'),

    path('videos_all/', views.get_all_videos, name='get_all_videos'),
    
    # URL pattern for get_complete_video view
    path('complete_video/<str:session_id>/', views.get_complete_video, name='get_complete_video'),
]