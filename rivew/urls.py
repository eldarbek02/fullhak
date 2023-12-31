from django.urls import path
from .views import LikeViewSet,CommentView


urlpatterns = [
    path('api/v1/posts/<int:pk>/like/', LikeViewSet.as_view({'post': 'toggle_like'})),
    path('api/v1/comment/', CommentView.as_view({'post': 'create', 'get': 'list'})),
    path('api/v1/comment/<int:pk>/', CommentView.as_view({'delete': 'destroy'})),
]
