from django.shortcuts import get_object_or_404
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.shared.utils.token_gen import account_activation_token
from apps.users.models import User
from apps.users.serializers.forgot_password_serializer import ForgotPasswordSerializer, ForgotPasswordActivateSerializer


class ForgotPasswordView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ForgotPasswordSerializer

    @swagger_auto_schema(tags=['Forgot password'])
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        user = get_object_or_404(User, email=email)

        response_data = {
            'message': f"We're have sent an email to {user.email} with further instructions.",
            'uidb64': urlsafe_base64_encode(force_bytes(str(user.pk))),
            'token': account_activation_token.make_token(user)
        }
        return Response(response_data, status=status.HTTP_200_OK)


class ForgotPasswordActivateView(UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ForgotPasswordActivateSerializer

    @swagger_auto_schema(tags=['Forgot password'])
    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uid = kwargs['uidb64']
        token = kwargs['token']
        try:
            uuid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uuid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'success': 'Thank you for your email confirmation. Now you can login your account.'},
                            status.HTTP_200_OK)
        return Response({'user not found'},
                        status.HTTP_404_NOT_FOUND)
