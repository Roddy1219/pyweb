from django.conf.urls import url
from mall import views

urlpatterns = [
    url(r'^$', views.MallIndexView.as_view(), name='mall_index'),
    url(r'^detail/$', views.MallDetailView.as_view(), name='mall_detail'),
    url(r'^order/$', views.MallOrderView.as_view(), name='mall_order'),
    url(r'^pay/$', views.MallPayView.as_view(), name='mall_pay'),
]
