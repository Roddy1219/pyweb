from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic.base import View


'''
商城首页
'''
class MallIndexView(View):
    def get(self, request):
        return render(request, 'mall/mall.html')

'''
商品详情页
'''
class MallDetailView(View):
    def get(self, request):
        return  render(request, 'mall/mallDetail.html')

'''
商品订单
'''
class MallOrderView(View):
    def get(self, request):
        return render(request, 'mall/mallOrder.html')

'''
商品购物车支付
'''
class MallPayView(View):
    def get(self, request):
        return render(request, 'mall/shoppingCar.html')