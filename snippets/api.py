class CommentCreateSerializer(serializers.Serializer):
    comment = serializers.CharField(required=True)
    ...

class CommentCreateAPIView(APIView):
    serializer_class = CommentCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    ...

urlpatterns = [
    path('news/<int:pk>/comments/add/', CommentCreateAPIView.as_view(), name='comment-create')
]
