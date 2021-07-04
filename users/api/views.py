from rest_framework.authentication import TokenAuthentication
from rest_framework import status, viewsets, permissions, generics
from users.models import UserProfile, CustomUser
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from users.api.serializers import (
    UserRegisterSerializer, ChangePasswordSerializer,
)


class UserRegisterAPIViewSet(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            if CustomUser.objects.filter(phoneNo=request.data['phoneNo']).exists():
                return Response(data="کاربری با این شماره موبایل وجود دارد", status=status.HTTP_400_BAD_REQUEST)
            user = CustomUser(
                phoneNo=request.data['phoneNo'],
            )
            password = request.data['password']
            re_password = request.data['re_password']

            if password != re_password:
                return Response(data="باید هر دو رمز برابر باشند", status=status.HTTP_400_BAD_REQUEST)
            user.set_password(password)
            user.save()
            token = Token.objects.get(user=user)
            data = {
                'user': user.phoneNo,
                'token': token.key
            }
            return Response(data, status=status.HTTP_201_CREATED)


class UpdatePassword(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(data='پسورد با موفقیت تغییر یافت. لطفا دوباره لاگین کنید',
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(data='با موفقیت خارج شدید', status=status.HTTP_200_OK)
