from .models import Registration
from .serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    users = Registration.objects.all()
    serializer = RegistrationSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_users(request):
    users = Registration.objects.all()
    serializer = RegistrationSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)