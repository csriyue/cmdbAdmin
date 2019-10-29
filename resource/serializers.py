from rest_framework import serializers
from .models import Idc, Server, Cabinet, Manufacturer, ProductModel


class IdcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idc
        fields = '__all__'



class CabinetSerializer(serializers.ModelSerializer):
    idc = IdcSerializer()
    class Meta:
        model = Cabinet
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    vendor = ManufacturerSerializer()
    class Meta:
        model = ProductModel
        fields = '__all__'








class ServerSerializer(serializers.ModelSerializer):
    # idc = IdcSerializer()
    # cabinet = CabinetSerializer()
    # model_name = ProductModelSerializer()

    def get_idc_name(self, idc_obj):
        try:
            return {
                "name": idc_obj.name,
                "id": idc_obj.id
            }
        except Exception as e:
            return {}

    def get_cabinet_name(self, idc_obj):
        try:
            return {
                "name": idc_obj.name,
                "id": idc_obj.id
            }
        except Exception as e:
            return {}

    def get_model_name(self, idc_obj):
        try:
            return {
                "name": idc_obj.model_name,
                "vendor": idc_obj.vendor.vendor_name
            }
        except Exception as e:
            return {}




    def to_representation(self, instance):
        idc_name = self.get_idc_name(instance.idc)
        cabinet_name = self.get_cabinet_name(instance.cabinet)
        model_name = self.get_model_name(instance.model_name)
        ret = super(ServerSerializer, self).to_representation(instance)
        ret["idc"] = idc_name
        ret["cabinet"] = cabinet_name
        ret["model_name"] = model_name
        return ret

    class Meta:
        model = Server
        fields = '__all__'
