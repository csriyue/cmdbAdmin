from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Idc,Server  ,  Cabinet , Manufacturer ,ProductModel
from .serializers import IdcSerializer,ServerSerializer , CabinetSerializer ,  ManufacturerSerializer , ProductModelSerializer
from pyzabbix import ZabbixAPI
from rest_framework import status
from rest_framework.response import Response


class IdcViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # zapi = ZabbixAPI("http://192.168.8.27/zabbix/api_jsonrpc.php")
        # zapi.login("Admin", "zabbix")
        # groupname = request.data.get("name",)
        # ret = zapi.hostgroup.create(name=groupname)
        # groupid = ret.get("groupids")[0]
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        zapi = ZabbixAPI("http://192.168.8.27/zabbix/api_jsonrpc.php")
        zapi.login("Admin", "zabbix")
        host = 'test123'
        ip = request.data.get("manage_ip",)
        groupid = request.data.get("idc",)
        ret = zapi.host.create(host=host, interfaces=[
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": "",
                "port": "10050"
            }], groups=groupid)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer


