from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import Group

@api_view(['POST','GET'])
def login(request):
    try:
        username = request.data.get('username')
        user = get_object_or_404(User, username=username)

        if not user.check_password(request.data.get('password')):
            return Response({'error': 'Invalid credentials'}, status=404)
        
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(instance=user)

        return Response({
            'token': token.key,
            'message': 'Login successful',
            'user': user_serializer.data
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['POST'])
def register(request):
    try:
        group_name = request.data.get('group', None)

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password', ''))
            user.save()

            # Add user to the specified group if provided
            if group_name:
                group = Group.objects.filter(name=group_name).first()
                if not group:
                    return Response({'error': 'Group not found'}, status=404)
                user.groups.add(group)

            # Create a token for the user
            token = Token.objects.create(user=user)

            return Response({
                'message': 'Registration successful',
                'token': token.key,
                'user': serializer.data
            }, status=201)
        
        return Response(serializer.errors, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    try:
        user = request.user
        if not user.is_authenticated:
            return Response({'error': 'Authentication required'}, status=401)

        user_serializer = UserSerializer(instance=user)
        return Response(user_serializer.data, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=500)