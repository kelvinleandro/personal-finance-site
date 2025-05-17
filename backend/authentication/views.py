from rest_framework import permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LogoutSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


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
