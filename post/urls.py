from django.urls import path
from .views import PostView

urlpatterns = [
    path('api/v1/posts/', PostView.as_view({'post': 'create', 'get': 'list'})),
    path('api/v1/posts/<int:pk>/', PostView.as_view({'delete': 'destroy','get':'retrieve'}))
]

