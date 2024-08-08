from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from .authentication import CustomJWTAuthentication


class UserRegisterView(APIView):
    parser_classes = [MultiPartParser, ]
    serializers_class = UserRegisterSRL

    @swagger_auto_schema(request_body=serializers_class)
    def post(self, request):
        serializer = self.serializers_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors)


class UserLoginView(APIView):
    @swagger_auto_schema(request_body=UserLoginSRL)
    def post(self, request):
        serializer = UserLoginSRL(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = UserModel.objects.filter(username=username, password=password).first()
            if user is None:
                raise AuthenticationFailed('User not found or incorrect password')
            else:
                refresh = RefreshToken.for_user(user)
                follow = FollowModel.objects.filter(user=user).first()
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                    'user_id': user.id,
                    'fullname': user.fullname,
                    'username': user.username,
                    'email': user.email,
                    'user_image': user.user_image.url,
                    'subscribers': follow.subscribers.count(),
                    'subscriptions': follow.subscriptions.count()
                }
                return Response(data, status=200)
        return Response(serializer.errors, status=400)


class TestView(APIView):
    authentication_classes = [CustomJWTAuthentication]

    def get(self, request):
        return Response('Hello World')
