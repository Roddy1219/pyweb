from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic.base import View

'''
系统首页
'''
class ProIndexView(View):
    def get(self, request):
        return render(request, 'project/home.html')

'''
课程首页
'''
class CourseIndexView(View):
    def get(self, request):
        return render(request, 'project/project.html')

'''
课程详情
'''
class CourseDetailView(View):
    def get(self, request):
        return render(request, 'project/projectDetail.html')

'''
微信支付
'''
class WechatPayView(View):
    def get(self, request):
        pass
