from django.db import models
import uuid
# Create your models here.


class Idc(models.Model):
    name = models.CharField("idc名称", max_length=30, help_text="idc名称")
    address = models.CharField("机房地址", max_length=255, null=True, blank=True, help_text="机房地址")
    leader = models.CharField("机房负责人", max_length=25, null=True, blank=True, help_text="机房负责人")
    remark = models.CharField("备注说明", max_length=255, null=True, blank=True, help_text="备注说明")

    class Meta:
        verbose_name = "机房信息"
        verbose_name_plural = verbose_name
        db_table = 'resource_idc'

    def __str__(self):
        return self.name


class Cabinet(models.Model):
    name            = models.CharField("机柜名称", max_length=50, help_text="机柜名称")
   # power_supply    = models.IntegerField("电源功率", help_text="电源功率")
    idc             = models.ForeignKey(Idc, verbose_name="所在机房", on_delete=models.CASCADE, help_text="所在机房")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'resources_cabinet'
        ordering = ["id"]


class Manufacturer(models.Model):
    vendor_name     = models.CharField("厂商名称", max_length=32, db_index=True, help_text="厂商名称")
    remark          = models.CharField("备注", max_length=300, null=True, blank=True, help_text="备注")

    def __str__(self):
        return self.vendor_name

    class Meta:
        db_table = 'resources_manufacturer'
        ordering = ["id"]


class ProductModel(models.Model):
    model_name      = models.CharField("型号名称", max_length=32, help_text="型号名称")
    vendor          = models.ForeignKey(Manufacturer, verbose_name="所属制造商", on_delete=models.CASCADE,  help_text="所属制造商")

    def __str__(self):
        return self.model_name

    class Meta:
        db_table = 'resources_productmodel'
        ordering = ["id"]


class Server(models.Model):
    model_name      = models.ForeignKey(ProductModel, verbose_name="服务器型号", default=None, on_delete=models.CASCADE, help_text="服务器型号")
    idc             = models.ForeignKey(Idc, verbose_name="所在机房", null=True, on_delete=models.CASCADE, help_text="所在机房")
    cabinet         = models.ForeignKey(Cabinet, verbose_name="所在机柜", null=True, on_delete=models.CASCADE, help_text="所在机柜")
   # cabinet_position= models.CharField("机柜内位置", max_length=32, null=True, help_text="机柜内位置")
    # manufacture_data = models.DateField("制造日期", null=True, help_text="制造日期")
    # warranty_time   = models.DateField("保修时间", null=True, help_text="保修时间")
    # purchasing_time = models.DateField("采购时间", null=True, help_text="采购时间")
    # power_supply    = models.IntegerField("电源功率", null=True, help_text="电源功率")
    # os              = models.CharField("操作系统", max_length=100, default=None, help_text="操作系统")
    # hostname        = models.CharField("主机名", max_length=50, default=None, db_index=True, help_text="主机名")
    manage_ip       = models.CharField("管理IP", max_length=32, default=None, db_index=True, help_text="管理IP")
    # server_cpu      = models.CharField("CPU信息", max_length=250, default=None, help_text="CPU信息")
    # disk            = models.CharField("硬盘信息", max_length=300, null=True, help_text="硬盘信息")
    # server_mem      = models.CharField("内存信息", max_length=100, default=None, help_text="内存信息")
    status          = models.CharField("服务器状态", max_length=32, null=True, db_index=True, help_text="服务器状态")
    # remark          = models.TextField("备注", null=True, help_text="备注")
    # last_check      = models.DateTimeField("上次检测时间", auto_now=True, help_text="上次检测时间")
    uuid            = models.UUIDField("UUID", max_length=100, auto_created=True, default=uuid.uuid4, editable=False, help_text="UUID")
    # sn              = models.CharField("SN", max_length=40, db_index=True, null=True, help_text="SN")
    # server_type     = models.IntegerField("机器类型", db_index=True, default=0, help_text="机器类型")
    """
        机器类型，0：vm, 1:物理机, 2:宿主机
    """

    def __str__(self):
        return self.uuid

    class Meta:
        db_table = 'resources_server'


