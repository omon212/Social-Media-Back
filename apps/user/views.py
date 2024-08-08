from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from .authentication import CustomJWTAuthentication
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken


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
                return Response(data, 200)
        return Response(serializer.errors, 400)


# class UserLogoutView(APIView):
#     authentication_classes = [CustomJWTAuthentication]
#
#     def post(self, request):
#         try:
#             refresh_token = request.data.get('refresh_token')
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response({"message": "Logged out successfully"}, status=200)
#         except Exception as e:
#             return Response({"error": str(e)}, status=400)
