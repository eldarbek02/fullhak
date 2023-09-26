from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from post.models import Posts
from .models import Favorite
from .serializers import FavoriteSerializer
from rest_framework import permissions



class IsFavoritePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class IsAuthorizedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated




class FavoriteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthorizedUser,IsFavoritePermissions]



    def list(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None):
        user = request.user
        post_id = pk


        try:
            post = Posts.objects.get(pk=post_id)
        except Posts.DoesNotExist:
            return Response({"error": "Пост не найден"}, status=status.HTTP_404_NOT_FOUND)

        # Проверяем, существует ли запись в избранном для данного пользователя и поста
        favorite, created = Favorite.objects.get_or_create(user=user, posts=post)

        if created:
            return Response({"message": "Пост добавлен в избранное"}, status=status.HTTP_201_CREATED)
        else:
            favorite.delete()
            return Response({"message": "Пост удален из избранного"}, status=status.HTTP_200_OK)
