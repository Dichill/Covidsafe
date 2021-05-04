from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

from knox.views import LoginView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer

from django.contrib.auth import login

# Register API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Login API
class LoginAPI(LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
