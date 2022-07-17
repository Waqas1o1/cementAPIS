import json
from xml.parsers import expat
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from app.models import Agent, Bank, CashInHandPerson, Company, Driver, ExpenseHead, Party
from authentications.serializer import UpdateUserSerializer, UserSerializer, RegisterSerializer
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

    def update(self,request, pk=None):
        user = User.objects.get(pk=pk)
        data = {**request.data}
        if "companies" in request.data:
            quires = request.data["companies"]
            quires = json.loads(quires)
            save_obj = []
            for id in quires:
                try:
                    obj = Company.objects.get(id=id)
                    save_obj.append(obj)
                except ObjectDoesNotExist:
                    pass 
            user.companies.set(save_obj)
            del data["companies"]
        if "parties" in request.data:
            quires = request.data["parties"]
            quires = json.loads(quires)
            save_obj = []
            for id in quires:
                try:
                    obj = Party.objects.get(id=id)
                    save_obj.append(obj)
                except ObjectDoesNotExist:
                    pass 
            user.parties.set(save_obj)
            del data["parties"]
        if "agents" in request.data:
            quires = request.data["agents"]
            quires = json.loads(quires)
            save_obj = []
            for id in quires:
                try:
                    obj = Agent.objects.get(id=id)
                    save_obj.append(obj)
                except ObjectDoesNotExist:
                    pass 
            user.agents.set(save_obj)
            del data["agents"]
        if "drivers" in request.data:
            quires = request.data["drivers"]
            quires = json.loads(quires)
            save_obj = []
            for id in quires:
                try:
                    obj = Driver.objects.get(id=id)
                    save_obj.append(obj)
                except ObjectDoesNotExist:
                    pass 
            user.drivers.set(save_obj)
            del data["drivers"]
        if "cash_in_hps" in request.data:
            quires = request.data["cash_in_hps"]
            quires = json.loads(quires)
            save_obj = []
            for id in quires:
                try:
                    obj = CashInHandPerson.objects.get(id=id)
                    save_obj.append(obj)
                except ObjectDoesNotExist:
                    pass 
            user.cash_in_hps.set(save_obj)
            del data["cash_in_hps"]
        if "banks" in request.data:
            quires = request.data["banks"]
            quires = json.loads(quires)
            save_obj = []
            for id in quires:
                try:
                    obj = Bank.objects.get(id=id)
                    save_obj.append(obj)
                except ObjectDoesNotExist:
                    pass 
            user.banks.set(save_obj)
            del data["banks"]
        if "expense_heads" in request.data:
            quires = request.data["expense_heads"]
            quires = json.loads(quires)
            save_obj = []
            for id in quires:
                try:
                    obj = ExpenseHead.objects.get(id=id)
                    save_obj.append(obj)
                except ObjectDoesNotExist:
                    pass 
            user.expense_heads.set(save_obj)
            del data["expense_heads"]



        serializer = UpdateUserSerializer(request.user, data=data, partial=True)
        serializer.is_valid()
            
        if serializer.errors:
            response = {"error":True,"message":serializer.errors}
        else:   
            serializer.save()
            response = {"error": False, "message": "Updated Successfuly"}
        return Response(response)


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
