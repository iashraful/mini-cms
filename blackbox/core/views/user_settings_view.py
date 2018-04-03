from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from blackbox.core.models.user_settings import Confirmation


class UserConfirmView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        response_data = {
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False
        }
        try:
            token = request.data.get('token')
            conf_entry = Confirmation.objects.get(token=token)
            user = conf_entry.user
            user.is_active = True
            user.save()
            # Now remove the entry from Confirmation Model
            conf_entry.delete()
            response_data['status'] = status.HTTP_200_OK
            response_data['success'] = True
            response_data['message'] = "User has activated successfully."
        except (ValidationError, AttributeError, ObjectDoesNotExist):
            response_data['message'] = "Invalid token for confirmation."
        return Response(data=response_data, status=response_data.get('status'))
