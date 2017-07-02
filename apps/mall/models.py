from datetime import datetime
from django.db import models


# Create your models here.

# 商品分类
class MallCategory(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='分类名')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name


# 商品实拍图
class MallImages(models.Model):
    img_name = models.CharField(max_length=100, verbose_name='图片名')
    img_url = models.ImageField(max_length=100, upload_to='image/%Y/%m', verbose_name='商品图片')

    def __str__(self):
        return self.img_name

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name


# 商品表
class MallCommodity(models.Model):
    name = models.CharField(max_length=50, verbose_name='商品名')
    category = models.ForeignKey(MallCategory)
    price = models.IntegerField(default=0, verbose_name='价格')
    browse_count = models.IntegerField(default=0, verbose_name='浏览量')
    stock_count = models.IntegerField(default=666, verbose_name='库存')
    image = models.ManyToManyField(MallImages)
    source = models.CharField(default='自拍图', max_length=50,verbose_name='主图来源')
    buy_count = models.IntegerField(default=0, verbose_name='购买量')
    color = models.CharField(max_length=50, verbose_name='颜色')
    model = models.CharField(max_length=100, verbose_name='型号')
    brand = models.CharField(max_length=50, verbose_name='品牌')
    discount = models.FloatField(default=10, verbose_name='折扣')
    description = models.TextField(verbose_name='商品描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品名'
        verbose_name_plural = verbose_name
