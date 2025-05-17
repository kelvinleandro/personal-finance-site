from rest_framework import generics, permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LogoutSerializer, RegisterSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class SignupView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Successfully logged out"}, status=status.HTTP_204_NO_CONTENT
        )
