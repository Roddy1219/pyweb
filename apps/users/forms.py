__author__ = 'luodi'
__date__ = '2017/06/10'

from django import forms

from captcha.fields import CaptchaField

from .models import UserProfile


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5, error_messages={'invalid': '密码长度太短!'})
    captcha = CaptchaField(error_messages={'invalid': '验证码错误！'})


class UserRegisterForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'invalid': '邮箱格式错误!'})
    mobile = forms.IntegerField(required=True, min_value=11, error_messages={'invalid': '手机号错误!'})
    password = forms.CharField(required=True, min_length=5, error_messages={'invalid': '密码长度太短!'})
    code = forms.IntegerField(required=True, min_value=5,error_messages={'invalid': '请输入正确的验证码!'})


class UserSendCodeForm(forms.Form):
    mobile = forms.IntegerField(required=True)
