from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^login/$', views.UserLoginView.as_view(), name='user_login'),
    url(r'^logout/$', views.UserLogoutView.as_view(), name='user_logout'),
    url(r'^register/$', views.UserRegisterView.as_view(), name='user_register'),
    url(r'^info/$', views.UserInfoView.as_view(), name='user_info'),
    url(r'^resetpw/$', views.UserPswView.as_view(), name='user_resetpw'),
    url(r'^collect/$', views.UserCollectView.as_view(), name='user_collect'),
    url(r'^recharge/$', views.UserVipView.as_view(), name='user_recharge'),
    url(r'^record/$', views.UserRecordView.as_view(), name='user_record'),
    url(r'^code/$', views.SendCodeView.as_view(), name='send_code'),
]
