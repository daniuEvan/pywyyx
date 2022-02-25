# Python 网易云信(短信验证码)  SDK
- [Golang SDK 网易云信(短信验证码)](https://github.com/daniuEvan/go-wysm)


- [网易云信官网地址]( https://yunxin.163.com)
- [网易云信短信功能开通说明](https://doc.yunxin.163.com/docs/DI1Mzc2NTU/TE1ODQ0NDY?platformId=120002)
- [官方短信验证码接口文档](https://doc.yunxin.163.com/docs/DI1Mzc2NTU/zA2MjExNzY?platformId=120002) 

## 环境依赖准备

```
pip install requests
```

## 发送短信验证码

```python
sm = SmService("你的手机号", "你的appkey", "app_secret", "短信模板id,[数字类型]")
print(sm.send_sm_code())
```

- 成功回resJson值, msg字段表示此次发送的sendid；obj字段表示此次发送的验证码。

  ```go
  {
    "code": 200,   // 状态码
    "msg": "88",   
    "obj": "1908"  // 验证码
  }
  ```

- 更多返回码请参考: https://doc.yunxin.163.com/docs/TM5MzM5Njk/Tk5ODIzNjk

## 校验短信验证码

```python
sm = SmService("你的手机号", "你的appkey", "app_secret", "短信模板id,[数字类型]")
print(sm.verity_sm_code("你的验证码"))
```

- 成功resJson返回值:

  ```go
  {
    "code":200
  }
  ```

- 更多返回码请参考: https://doc.yunxin.163.com/docs/TM5MzM5Njk/Tk5ODIzNjk
  