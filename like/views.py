from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer
from post.models import Posts

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    # Метод для добавления или удаления лайка
    @action(detail=True, methods=['patch'])
    def toggle_like(self, request, pk=None):
        like = self.get_object()
        user = request.user
        post = like.post

        # Проверка, может ли пользователь лайкнуть/дизлайкнуть
        if user == like.author:
            return Response({"detail": "Вы не можете лайкнуть/дизлайкнуть свой собственный пост."}, status=400)

        if Like.objects.filter(post=post, author=user).exists():
            # Если лайк уже существует, удаляем его
            Like.objects.filter(post=post, author=user).delete()
            return Response({"message": "Лайк удален"}, status=200)
        else:
            # Иначе, создаем новый лайк
            Like.objects.create(post=post, author=user)
            return Response({"message": "Лайк добавлен"}, status=201)
