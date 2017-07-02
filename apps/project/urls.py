from django.conf.urls import url
from project import views

urlpatterns = [
    url(r'^$', views.CourseIndexView.as_view(), name='course_index'),
    url(r'^detail/$', views.CourseDetailView.as_view(), name='course_detail'),
    url(r'^pay/$', views.WechatPayView.as_view(), name='course_pay'),
]