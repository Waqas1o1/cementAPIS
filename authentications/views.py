from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from authentications.serializer import UserSerializer, RegisterSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth.models import Group
from .models import User
from . import serializer as s
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

# from app import models as m
# Register API


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        dict_response = {"user": user.username, "error": False}

        return Response(dict_response)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        temp_list = super(LoginAPI, self).post(request, format=None)
        temp_list.data['user'] = UserSerializer(user, many=False).data

        return Response({"data": temp_list.data})


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        data = User.objects.all().order_by('-id')
        serializer = s.UserSerializer(
            data, many=True, context={"request": request})
        response_dict = {"error": False,
                         "message": "All List Data", "data": serializer.data}
        return Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = User.objects.all()
            recovery = get_object_or_404(queryset, pk=pk)
            serializer = s.UserSerializer(
                recovery, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {"error": False,
                             "message": "Successfully Updated Data"}
        except:
            response_dict = {"error": True,
                             "message": serializer.errors}

        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        query = get_object_or_404(queryset, pk=pk)
        serializer = s.UserSerializer(
            query, context={"request": request})
        serializer_data = serializer.data

        return Response({"error": False, "message": "Single Data Fetch", "data": serializer_data})

    def delete(self, request, pk=None):
        try:
            User.objects.get(id=pk).delete()
            response_dict = {"error": False,
                             "message": "Successfully Deleted"}
        except:
            response_dict = {"error": True,
                             "message": "Error During Deleted Data "}

        return Response(response_dict)


class UserFilter(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = s.UserSerializer
    name = 'User-list'
    filter_backends = [SearchFilter]

    search_fields = (
        "$username",
        "$first_name",
        "$last_name",
        "$email"
    )
