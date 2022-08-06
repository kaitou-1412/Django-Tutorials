from django.urls import path, include
# from .views import movie_list, movie_details
from rest_framework.routers import DefaultRouter

from .views import ReviewCreate, ReviewList, ReviewDetail, WatchListAV, WatchDetailAV, StreamPlatformVS, UserReview, \
    WatchListGV

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watchlist-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watchlist-detail'),
    path('list2/', WatchListGV.as_view(), name='watch-list'),

    path('', include(router.urls)),

    # path('stream/list/', StreamPlatformListAV.as_view(), name='streamplatform-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    # path('reviews/<str:username>/', UserReview.as_view(), name='user-review-detail'),
    path('reviews/', UserReview.as_view(), name='user-review-detail'),
]
