## 准备

* 注册[Server酱](http://sc.ftqq.com/)，获取`SCKEY`，修改脚本`index.py`中的`sckey`
> 用来通知微信提醒签到获得了多少V力值和**Cookie失效**，如果你不打算通知或者有其他方式，可以跳过

* 需要一台有`Python2`环境的`Linux`服务器或者使用[腾讯云Serverless](https://console.cloud.tencent.com/scf)
> 用来定时执行脚本

## 获取Cookie

1. 电脑打开浏览器访问`v.qq.com`，打开控制台(`F12`)、切换到Network，找到 `https://access.video.qq.com/user/auth_refresh` 的接口，把`Request URL:`后的地址都复制一下，填写到脚本的`auth_refresh_url`中，如：

![获取auth_refresh接口](https://cdn.jsdelivr.net/gh/sy-records/v-checkin@master/images/get-auth_refresh.png)

```python
auth_refresh_url = 'https://access.video.qq.com/user/auth_refresh?vappid=11059694&vsecret=********&type=qq&g_tk=&g_vstk=********&g_actk=********&callback=jQuery191048649********_1575435********4&_=1575435********'
```

> 可以搜索`auth_refresh`进行过滤

2. 还是`auth_refresh`这个接口，复制`Request Header`中的`cookie`，填写到脚本的`login_headers`的`Cookie`中

![获取cookie](https://cdn.jsdelivr.net/gh/sy-records/v-checkin@master/images/get-cookie.png)

```python
login_headers = {
    'Referer': 'https://v.qq.com',
    'Cookie': 'tvfe_boss_uuid=********; pgv_pvid=********; video_guid=***********; video_platform=2; pgv_info=ssid=***********; pgv_pvi=*************; pgv_si=*************; _qpsvr_localtk=***************; ptisp=; ptui_loginuin=************; RK=*************; ptcz=***************; main_login=qq; vqq_access_token=****************; vqq_appid=101483052; vqq_openid=********************; vqq_vuserid=*********************; vqq_vusession=dzsfo; vqq_refresh_token=*****************; uid=**************;'
}
```

3. 重复第二步，粘贴到脚本中的`sign_headers`的`Cookie`中，注意修改`vqq_vusession`，变量`cookie['vqq_vusession']`需要保留不要替换

> 说明：等于把第二步中获取到的`Cookie`的`vqq_vusession=dzsfo;`放到末尾，并且修改为`vqq_vusession=`

```python
sign_headers = {
    'Cookie': 'tvfe_boss_uuid=***********; pgv_pvid=***************; video_guid=***************; video_platform=2; pgv_info=ssid=****************; pgv_pvi=****************; pgv_si=***************; _qpsvr_localtk=*************; ptisp=; ptui_loginuin=***************; RK=****************; ptcz=*********************; main_login=qq; vqq_access_token=************; vqq_appid=101483052; vqq_openid=*************; vqq_vuserid=*************; vqq_vusession=' + cookie['vqq_vusession'] + ';'
}
```
