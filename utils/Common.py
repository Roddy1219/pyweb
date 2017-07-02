import random
from urllib import request,parse



class sendMsg(object):
    def __init__(self,mobile):
        self.mobile=mobile
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.url = 'http://jk.106api.cn/smsUTF8.aspx'  # 如连接超时，可能是您服务器不支持域名解析，请将下面连接中的：【api.sms998.cn】修改为IP：【123.56.186.169:555】
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.username = '3542769256'  # 用户名
        self.password_md5 = '85FEE13794C9B1E3754317807395B24B'  # 32位MD5密码加密
        self.gwid = '3fe0a05'  # 登录平台->首页获取网关ID


    def send(self, code):
        message = "您的验证码为:"+str(code)+",如非本人操作请忽略。【世纪阳天】"  # 要发送的短信内容，特别注意：网页验证码应用需要加添加【图形识别码】以防被短信攻击
        values = {
            'type': 'send',
            'username': self.username,
            'password': self.password_md5,
            'gwid': self.gwid,
            'mobile': self.mobile,
            'message': message
        }
        headers = {'User-Agent': self.user_agent}
        data = parse.urlencode(values).encode('utf8')
        req = request.Request(self.url, data, headers=headers)
        response = request.urlopen(req)
        # 发送并把结果赋给result,返回一个XML信息,解析xml 信息判断
        response.read().decode('UTF-8')
    def randomCode(self):
        data = random.randint(100000, 999999)
        return data