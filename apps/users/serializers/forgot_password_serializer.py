from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import EmailField, ModelSerializer

from apps.users.models import User


class ForgotPasswordSerializer(ModelSerializer):
    email = EmailField(
        required=True,
    )

    class Meta:
        model = User
        fields = ('email',)


class ForgotPasswordActivateSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise ValidationError({"password": "Password fields didn't match."})

        return attrs

    class Meta:
        model = User
        fields = ('password', 'confirm_password',)
