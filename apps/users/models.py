from django.db import models

# Create your models here.

from datetime import datetime

from django.db import models
from project.models import Course

from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='female', verbose_name='性别')
    address = models.CharField(max_length=100, default='', verbose_name='地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    image = models.ImageField(max_length=100, upload_to='image/%Y/%m', default='image?default.png', verbose_name='头像')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=18, choices=(('register', '邮箱'), ('forget', '修改密码'), ('update_email', '修改邮箱')),
                                 verbose_name='验证码类型')
    send_time = models.DateField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = '邮箱验证码'


class SmsVerifyRecord(models.Model):
    code = models.IntegerField(default=0,verbose_name='手机验证码')
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name='发送手机')
    status= models.IntegerField(default=1,verbose_name='状态')
    send_time = models.DateTimeField(default=datetime.now,verbose_name='发送时间')
    token = models.CharField(max_length=50,default=None)

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', max_length=100, verbose_name='轮播图')
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


#用户充值记录
class RechargeHistory(models.Model):
    recharge_id = models.CharField(max_length=50,verbose_name='充值单号')
    amount = models.FloatField(default=0,verbose_name='充值金额')
    time =  models.DateTimeField(default=datetime.now,verbose_name='充值时间')
    user = models.ForeignKey(UserProfile)
    status = ((1, '成功'),
              (0, '未成功')
              )
    recharge_status = models.IntegerField(default=0,choices=status,verbose_name='充值状态')

    class Meta:
        verbose_name = '用户充值表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.recharge_id



#用户购买记录
class BuyHistory(models.Model):
    mall_id = models.CharField(max_length=50,verbose_name='商品ID')
    mall_amount = models.CharField(max_length=50,verbose_name='商品金额')
    mall_count = models.IntegerField(default=1,verbose_name='数量')
    buy_user = models.ForeignKey(UserProfile,verbose_name='购买用户')
    buy_time = models.DateTimeField(default=datetime.now,verbose_name='购买时间')
    status = ((1,'成功'),
              (0,'失败'),
              (-1,'未支付'),
              )
    buy_status = models.IntegerField(default=-1,choices=status,verbose_name='购买状态')
    order_id = models.CharField(max_length=50,verbose_name='订单ID')

    buy_select = ((1,'微信'),
                  (2,'支付宝'),
                  (3,'余额')
                  )
    buy_type = models.IntegerField(default=0,choices=buy_select,verbose_name='付款方式')

    class Meta:
        verbose_name = '购买记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.mall_id


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    # ID 是课程的 ID 或者是 讲师、课程机构的 ID
    fav_id = models.IntegerField(default=0, verbose_name='收藏数据 Id')
    fav_type = models.IntegerField(choices=( (1, '课程'), (2, '课程机构'), (3, '讲师') ), default=1, verbose_name='收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

    # 初始化判断是否收藏
    # has_fav = False
    # if request.user.is_authenticated():
    #     if UserProfile.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
    #         has_fav = True


class UserMessage(models.Model):
    # 如果 为 0 代表全局消息，否则就是用户的 ID
    user = models.IntegerField(default=0, verbose_name='接受用户')
    message = models.CharField(max_length=500, verbose_name='消息内容')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


# CourseComments 和 UserCourse 字段差不多，可以使用 UserCourse 继承 CourseComments
class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    course = models.ForeignKey(Course, verbose_name='课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户学习过的课程'
        verbose_name_plural = verbose_name










