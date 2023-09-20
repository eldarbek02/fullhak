from django.urls import path
from .views import LikeViewSet

urlpatterns = [
        path('api/v1/<int:pk>/', LikeViewSet.as_view({'put': 'toggle_like'})),
    
]
