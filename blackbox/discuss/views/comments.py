from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from blackbox.discuss.enums.comment_enums import CommentTypeEnum
from blackbox.discuss.models import Comment
from blackbox.discuss.serializers.comments import CommentSerializer

__author__ = 'Ashraful'


class CommentListView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        _user = self.request.is_authenticated
        if _user:
            return Comment.objects.all()
        else:
            return Comment.objects.filter(status=CommentTypeEnum.Accepted.value)


class CommentDetailsView(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer

    def get_object(self):
        uuid = self.kwargs.get('uuid')
        try:
            obj = Comment.objects.get(uuid=uuid)
            return obj
        except Exception:
            return None
