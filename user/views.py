from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer


class UserList(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as err:
            print(f'Err get: {err}')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(password=request.data['password'])
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print(f'Err post: {err}')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def put(self, request):
        try:
            user = User.objects.get(pk=request.data.get('id'))        
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': 'User update'}, status=status.HTTP_200_OK)
        except Exception as err:
            print(f'Err put: {err}')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = User.objects.get(pk=request.data.get('id'))
            if user:
                user.delete()
                return Response({'msg': 'User delete'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'msg': "User doesn't exist"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Exception as err:
            print(f'Err delete: {err}')
            return Response({'msg': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)