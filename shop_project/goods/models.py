from django.db import models

# Create your models here.
from django.db import models

# 学生/商户模型
class Student(models.Model):
    username = models.CharField(max_length=50, verbose_name="姓名")
    phone = models.CharField(max_length=11, verbose_name="手机号")
    gender = models.CharField(max_length=10, choices=[("男","男"),("女","女")], verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    class_name = models.CharField(max_length=30, verbose_name="所属班级", default="未填写")
    is_seller = models.BooleanField(default=False, verbose_name="是否开通商户权限")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.username

# 商品模型
class Goods(models.Model):
    name = models.CharField(max_length=100, verbose_name="商品名称")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
    category = models.CharField(max_length=50, verbose_name="分类")
    description = models.TextField(verbose_name="商品描述")
    image = models.ImageField(upload_to='goods/', null=True, blank=True, verbose_name="商品图片")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="发布商户")

    def __str__(self):
        return self.name