from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from stocks.serializers import ToySerializer, UsersSerializer, BasketSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from stocks.models import *


class ToyViewSet(viewsets.ModelViewSet):
    queryset = Toy.objects.all().order_by('pk')
    serializer_class = ToySerializer  # Сериализатор для модели

    def get_queryset(self):
        requested_toys = [int(id) for id in self.request.query_params.getlist('id')]
        queryset = Toy.objects.all()
        if len(requested_toys) > 0:
            queryset = queryset.filter(pk__in=requested_toys)
        return queryset


    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None

        }
        return Response(content)


class UsersViewSet(viewsets.ModelViewSet):
    # queryset всех пользователей для фильтрации
    queryset = User.objects.all().order_by('pk')
    serializer_class = UsersSerializer  # Сериализатор для модели


class BasketViewSet(viewsets.ModelViewSet):
    # queryset всех пользователей для фильтрации
    queryset = Basket.objects.all().order_by('pk')
    serializer_class = BasketSerializer  # Сериализатор для модели

    def get_queryset(self):
        user_pk = self.request.query_params.get('user')
        queryset = Basket.objects.all()
        if user_pk is not None:
            queryset = queryset.filter(user=user_pk)
        return queryset

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class Registration(APIView):
    def post(self, request, format=None):
        data = self.request.data
        username = data['username']
        password = data['password']
        if User.objects.filter(username = username).exists():
            return Response({'error':'Username already exists'})
        else:
            user = User.objects.create_user( username=username, password=password)
            user.save()
        return Response({'success': 'User created'});


class Check(APIView):
    def get(self, request, format=None):
        user = self.request.user
        isAuthenticated = user.is_authenticated

        if isAuthenticated:
            return Response({'isAuthenticated':'success'})
        else:
            return Response({'isAutheticated': 'error'})


class LoginView(APIView):
    def post(self, request, format=None):
        data = self.request.data
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        usr=User.objects.get(username=username)
        if user is not None:
            login(request, user)
            return Response({'success':'User authenticated', 'username': username, 'pk':user.pk,  'is_staff': usr.is_staff})
        else:
            return Response({'error':'Error Authenticated'})


class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            logout(request)
            return Response({'success': 'User Logout'})
        except:
            return Response({'error': 'Error logout'})