from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, JsonResponse
from django.core.urlresolvers import reverse

from django.views.generic.base import View

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login, logout
from users import models
from django.db.models import Q
from django.conf import settings as django_settings
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password

from .forms import UserLoginForm, UserRegisterForm, UserSendCodeForm

from .models import UserProfile, SmsVerifyRecord
from itsdangerous import TimestampSigner
from utils.Common import sendMsg



# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = models.UserProfile.objects.get(Q(email=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


'''
用户登录处理
'''


class UserLoginView(View):
    def get(self, request):
        login_form = UserLoginForm()
        return render(request, 'users/login.html', {'login_form': login_form})

    def post(self, request):

        '''login form check'''
        login_form = UserLoginForm(request.POST)

        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')

        user = authenticate(username=user_name, password=pass_word)

        if login_form.is_valid():
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponsePermanentRedirect(reverse('pro_index'))
                else:
                    return render(request, 'users/login.html',
                                  {'msg': '用户未激活！', 'login_form': login_form, 'data': login_form.clean()})

            return render(request, 'users/login.html',
                          {'msg': '用户名或密码错误！', 'login_form': login_form, 'data': login_form.clean()})

        return render(request, 'users/login.html',
                      {'form_errors': login_form.errors, 'login_form': login_form, 'data': login_form.clean()})


'''
用户注册
'''


class UserRegisterView(View):
    def get(self, request):
        register_form = UserRegisterForm()
        return render(request, 'users/register.html', {'register_form': register_form})

    def post(self, request):

        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():

            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email):
                return render(request, 'users/register.html', {'register_form': register_form, 'msg': '用户已存在','data': register_form.clean()})
            mobile = request.POST.get('mobile', '')

            if UserProfile.objects.filter(mobile=mobile):
                return render(request, 'users/register.html',
                              {'register_form': register_form, 'mobile_msg': '手机号已使用', 'data': register_form.clean()})

            code = request.POST.get('code','')

            if not SmsVerifyRecord.objects.filter(code=code,mobile=mobile):
                return render(request, 'users/register.html', {'register_form': register_form, 'msg': '验证码错误','data': register_form.clean()})

            #获取code所生成的时间token
            token_key = SmsVerifyRecord.objects.get(code=code,mobile=mobile,status=1)
            try:
                s = TimestampSigner(django_settings.SECRET_KEY)
                #如果验证码超过5分钟将报错
                s.unsign(token_key.token, max_age=300)
            except:
                return render(request, 'users/register.html', {'register_form': register_form, 'msg': '验证码过期','data': register_form.clean()})
            else:
                password = request.POST.get('password', '')
                user_profile = UserProfile()
                user_profile.username = email
                user_profile.email = email
                user_profile.mobile = mobile
                print(password)
                user_profile.password = make_password(password)
                user_profile.is_active = True
                user_profile.save()

                #验证码已使用
                token_key.status = 0
                token_key.save()

                return HttpResponsePermanentRedirect(reverse('pro_index'))
        else:
            return render(request,'users/register.html',{'register_form':register_form,'data': register_form.clean()})


'''
用户退出
'''


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('pro_index'))


'''
用户信息展示
'''


class UserInfoView(View):
    def get(self, request):
        return render(request, 'users/userInfo.html')


'''
用户充值页面
'''


class UserVipView(View):
    def get(self, request):
        return render(request, 'users/userRecharge.html')


'''
用户修改密码
'''


class UserPswView(View):
    def get(self, request):
        return render(request, 'users/userPsw.html')


'''
用户购买记录
'''


class UserRecordView(View):
    def get(self, request):
        return render(request, 'users/userRecord.html')


'''
课程收藏
'''


class UserCollectView(View):
    def get(self, request):
        return render(request, 'users/userCollect.html')


'''
发送短信接口
'''


class SendCodeView(View):
    def get(self, request):
        print(request.GET.get('mobile'))
        user_send_code = UserSendCodeForm(request.GET)
        if user_send_code.is_valid():
            mobile = request.GET.get('mobile', '')

            # 生成验证码
            sendsms = sendMsg(mobile)
            code = sendsms.randomCode()
            sendStatus = sendsms.send(code)
            s = TimestampSigner(django_settings.SECRET_KEY)
            token_key = s.sign(str(code))
            savecode = SmsVerifyRecord.objects.create(code=code, mobile=mobile, status=1, token=token_key)
            savecode.save()
            return JsonResponse({'code': 1, 'msg': ''})

        return JsonResponse({'code': 0, 'msg': user_send_code.errors})
