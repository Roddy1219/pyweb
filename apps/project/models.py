from django.db import models
from datetime import datetime

# Create your models here.


# 课程分类
class CourseCategory(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='分类名')
    create_at = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = '课程分类'
        verbose_name_plural = verbose_name

# 讲师
class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name='讲师姓名')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=50, verbose_name='就职公司')
    work_position = models.CharField(max_length=50, verbose_name='公司职位')
    age = models.IntegerField(default=30, verbose_name='年龄')
    image = models.ImageField(default='', upload_to='tearcher/%Y/%m', verbose_name='头像', max_length=100)
    create_at = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '讲师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#课程表
class Course(models.Model):
    name = models.CharField(max_length=52,verbose_name='课程名')
    desc = models.CharField(max_length=300,verbose_name='课程描述')
    teacher = models.ForeignKey(Teacher,verbose_name='讲师', null=True,blank=True)
    detail = models.TextField(verbose_name='课程详情')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图', max_length=100)
    category = models.ForeignKey(CourseCategory,verbose_name='课程分类')
    tag = models.CharField(default='',verbose_name='课程标签', max_length=10)
    need_know = models.CharField(default='',max_length=300,verbose_name='课前须知')
    teacher_tell = models.CharField(default='',max_length=300,verbose_name='能学到什么')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#课程章节
class Lesson(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=100,verbose_name='章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')


    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name




class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名')
    url = models.URLField(max_length=200, verbose_name='访问地址', default='www.baidu.com')
    learn_times = models.IntegerField(default=0, verbose_name='视频时长(分钟数)')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name





