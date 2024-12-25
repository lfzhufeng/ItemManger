from django.db import models
from django.conf import settings

# 订单状态
class OrderStatus(models.IntegerChoices):
    PENDING = 0, "待付款"
    PAID = 1, "已付款"
    CANCELED = 2, "已取消"

# 支付方式
class PaymentMethod(models.IntegerChoices):
    WECHAT = 0, "微信支付"
    ALIPAY = 1, "支付宝"

# 支付状态
class PaymentStatus(models.IntegerChoices):
    PENDING = 0, "处理中"
    SUCCESS = 1, "成功"
    FAILED = 2, "失败"

# 订单表
class Order(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="订单ID")
    order_number = models.CharField(max_length=30, unique=True, verbose_name="订单编号")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="用户")
    status = models.IntegerField(choices=OrderStatus, default=OrderStatus.PENDING, verbose_name="订单状态")
    payable_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="支付金额")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    description = models.TextField(blank=True, null=True, verbose_name="订单备注")
    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")


    class Meta:
        db_table = 'orders'  # 设置自定义表名为 'custom_user'
        verbose_name = '订单'  # 管理界面显示的名称（单数）
        verbose_name_plural = '订单列表'  # 管理界面显示的名称（复数）
    def __str__(self):
        return self.order_number

# 支付记录表
class Payment(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="支付记录ID")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments", verbose_name="关联订单")
    payment_number = models.CharField(max_length=50, unique=True, verbose_name="支付流水号")
    payment_method = models.IntegerField(choices=PaymentMethod, verbose_name="支付方式")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="支付金额")
    payment_status = models.IntegerField(choices=PaymentStatus, default=PaymentStatus.PENDING, verbose_name="支付状态")
    transaction_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="支付网关交易号")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'payment'  # 设置自定义表名为 'custom_user'
        verbose_name = '支付记录'  # 管理界面显示的名称（单数）
        verbose_name_plural = '支付记录列表'  # 管理界面显示的名称（复数）
    def __str__(self):
        return self.payment_number
