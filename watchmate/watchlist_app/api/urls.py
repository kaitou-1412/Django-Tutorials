from django.urls import path, include
# from .views import movie_list, movie_details
from .views import WatchListAV, WatchDetailAV, StreamPlatformListAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch-detail'),
    path('stream/list/', StreamPlatformListAV.as_view(), name='stream-platform-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-platform-detail'),
]
