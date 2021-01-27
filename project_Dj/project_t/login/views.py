from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.template import RequestContext
import time
from django.http import HttpResponseRedirect


# Create your views here.


def login(request):
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if request.method == 'GET':
        # return render_to_response('login/login.html', {'nowtime': nowtime})
        return render_to_response('test/testLogin.html', {'nowtime': nowtime})
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = ""
        # print(username,password)
        user = auth.authenticate(username=username, password=password)
        if user is None:
            # return render(request, 'login/login.html', {'status': "5001", 'message': "用户名或密码错误", 'nowtime': nowtime})
            return render(request, 'test/testLogin.html', {'status': "5001", 'message': "用户名或密码错误", 'nowtime': nowtime})

        # return render(request, 'dashboard.html', {'status': "2000", "username": username, "mail": email,
        #                                                           "message": "登录成功", 'nowtime': nowtime})
        else:
            auth.login(request, user)

            # 两种重定向方式都可以；一个不能传参。一个能传参

            return HttpResponseRedirect('/overview', RequestContext(request,
                                                                  {'status': "2000", "username": username,
                                                                   "message": "登录成功", 'nowtime': nowtime}))

            # return render_to_response('login/index.html',{'status': "200", 'message': "登录成功", 'username':username,'nowtime': nowtime})


