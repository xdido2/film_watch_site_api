from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.shared.utils.token_gen import account_activation_token
from apps.users.models import User
from apps.users.serializers.register_serializer import RegisterSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response_data = {
            'message': 'User registered successfully, check your email for activate your account!',
            'uidb64': urlsafe_base64_encode(force_bytes(str(user.pk))),
            'token': account_activation_token.make_token(user)
        }

        return Response(response_data, status=status.HTTP_201_CREATED)


class ActivateAccountView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        uid = kwargs['uidb64']
        token = kwargs['token']
        try:
            uuid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uuid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'success': 'Thank you for your email confirmation. Now you can login your account.'},
                            status.HTTP_200_OK)
        return Response({'user not found'},
                        status.HTTP_404_NOT_FOUND)
