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

    def perform_create(self, serializer):
        idc = serializer.save()
        zapi = ZabbixAPI("http://192.168.8.27/zabbix/api_jsonrpc.php")
        zapi.login("Admin", "zabbix")
        groupname = idc.name
        ret = zapi.hostgroup.create(name=groupname)
        idc.zbgroupid = ret.get("groupids")[0]
        idc.save()


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def perform_create(self, serializer):
        server = serializer.save()
        zapi = ZabbixAPI("http://192.168.8.27/zabbix/api_jsonrpc.php")
        zapi.login("Admin", "zabbix")

        host = str(server.uuid)
        ip = server.manage_ip
        groupid = server.idc.zbgroupid
        ret = zapi.host.create(host=host, interfaces=[
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": "",
                "port": "10050"
            }], groups=[{"groupid": groupid}])
        server.zbhostid = ret.get("hostids")[0]
        server.save()


class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer


