from django.urls import path
from .views import FavoriteViewSet

urlpatterns = [
    path('api/v1/favorit/', FavoriteViewSet.as_view({'get':'list'})),
    path('api/v1/favorit/<int:pk>/', FavoriteViewSet.as_view({'post':'create'})),
]
