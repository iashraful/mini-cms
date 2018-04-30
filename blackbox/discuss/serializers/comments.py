from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from blackbox.discuss.enums.comment_enums import CommentTypeEnum
from blackbox.discuss.models import Comment

__author__ = 'Ashraful'


class ReplySerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('uuid', 'text', 'status')


class CommentSerializer(ModelSerializer):
    replies = SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ('uuid', 'text', 'status', 'replies')
        lookup_filed = 'uuid'

    def get_replies(self, obj):
        replies = obj.replies.order_by('-updated_at')
        _request = self.context.get('request')
        if _request and not _request.user.is_authenticated:
            replies = replies.filter(status=CommentTypeEnum.Accepted.value)
        data = ReplySerializer(replies, many=True)
        return data.data
