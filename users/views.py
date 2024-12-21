from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, UserDetailSerializer


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
            user = User.objects.all()
            serializer = UserSerializer(user, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)

class UserDetailView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk = pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class AuthUserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserDetailSerializer(user) # 역직렬화를 해서 serializer 로 감싸고
        return Response(serializer.data, status = status.HTTP_200_OK) # 내보내준다