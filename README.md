## 准备

* `Fork` 本项目
* 注册`企业微信机器人`


## 配置Actions secrets

1. 电脑打开浏览器访问`v.qq.com`，打开控制台(`F12`)、切换到Network，找到 `https://access.video.qq.com/user/auth_refresh` 的接口，把`Request URL:`后的地址都复制一下，然后点击项目中的`Settings` --> `Secrets` --> `New repository secret`, `Name`值为`AUTH_REFRESH_URL` , `Value`值为`Request URL:后的地址`
例：
```
Request URL: https://access.video.qq.com/user/auth_refresh?vappid=1234567&vsecret=********&type=qq&g_tk=&g_vstk=********&g_actk=********&callback=jQuery191048649********_1575435********4&_=1575435********
```
`Value`值只取`https://access.video.qq.com/user/auth_refresh?vappid=1234567&vsecret=********&type=qq&g_tk=&g_vstk=********&g_actk=********&callback=jQuery191048649********_1575435********4&_=1575435********`


2. 依旧找到`https://access.video.qq.com/user/auth_refresh`这个接口，复制`Request Header`中的`cookie`，然后点击项目中的`Settings` --> `Secrets` --> `New repository secret`, `Name`值为`LOGIN_COOKIE` , `Value`值为`Request Header中的cookie`

例：
```
cookie: RK=T+S5fhzfX8; ptcz=930*******************************b8f0a7; tvfe_boss_uuid=468a9******; pgv_pvid=3565****6; video_guid=ad9841*****9; video_platform=2; ptui_loginuin=199******; main_login=qq; vqq_access_token=32*************; vqq_appid=10*********; vqq_openid=1**************; vqq_vuserid=1******; vqq_refresh_token=CA*****************; pgv_info=ssid=s84********; vqq_vusession=O1iwDP*****6ntxrWA..; uid=2*****; vqq_next_refresh_time=6525; vqq_login_time_init=1*****; login_time_last=****
```
`Value`值只取`RK=T+S5fhzfX8; ptcz=930*******************************b8f0a7; tvfe_boss_uuid=468a9******; pgv_pvid=3565****6; video_guid=ad9841*****9; video_platform=2; ptui_loginuin=199******; main_login=qq; vqq_access_token=32*************; vqq_appid=10*********; vqq_openid=1**************; vqq_vuserid=1******; vqq_refresh_token=CA*****************; pgv_info=ssid=s84********; vqq_vusession=O1iwDP*****6ntxrWA..; uid=2*****; vqq_next_refresh_time=6525; vqq_login_time_init=1*****; login_time_last=****`

3. 复制第二步中的`cookie`，然后将`cookie`中的`vqq_vusession=O1iwDP*****6ntxrWA..;`删除，然后点击项目中的`Settings` --> `Secrets` --> `New repository secret`, `Name`值为`SIGNIN_COOKIE` , `Value`值为`删除掉vqq_vusession=O1iwDP*****6ntxrWA..;`后的值

例：

去除前
```
RK=T+S5fhzfX8; ptcz=930*******************************b8f0a7; tvfe_boss_uuid=468a9******; pgv_pvid=3565****6; video_guid=ad9841*****9; video_platform=2; ptui_loginuin=199******; main_login=qq; vqq_access_token=32*************; vqq_appid=10*********; vqq_openid=1**************; vqq_vuserid=1******; vqq_refresh_token=CA*****************; pgv_info=ssid=s84********; vqq_vusession=O1iwDP*****6ntxrWA..; uid=2*****; vqq_next_refresh_time=6525; vqq_login_time_init=1*****; login_time_last=****
```

去除后
```
RK=T+S5fhzfX8; ptcz=930*******************************b8f0a7; tvfe_boss_uuid=468a9******; pgv_pvid=3565****6; video_guid=ad9841*****9; video_platform=2; ptui_loginuin=199******; main_login=qq; vqq_access_token=32*************; vqq_appid=10*********; vqq_openid=1**************; vqq_vuserid=1******; vqq_refresh_token=CA*****************; pgv_info=ssid=s84********; uid=2*****; vqq_next_refresh_time=6525; vqq_login_time_init=1*****; login_time_last=****
```
4. 点击项目中的`Settings` --> `Secrets` --> `New repository secret`, `Name`值为`KEY` , `Value`值为`https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx-xxxx-xxxx-xxxx-xxxx`中的`xxxx-xxxx-xxxx-xxxx-xxxx`
5. 点击 `Actions` 再点击 `I understand my workflows, go ahead and enable them`
6. 首次使用需手动点击一次 `Start`
