#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# date: 2022/2/25
# desc: 网易云信短信验证码
import hashlib
import random
import time
import traceback

import requests


class SmService(object):
    def __init__(self, mobile: str, app_key: str, app_secret: str, sm_template_code: int = 19506299, code_len: int = 4):
        """
        :param mobile: 手机号
        :param app_key: 网易云信 app key
        :param app_secret:网易云信 app secret
        :param sm_template_code: 网易云信 短信模板id
        :param code_len: 验证码长度
        """
        self.mobile = mobile
        self.app_secret = app_secret
        self.app_key = app_key
        self.sm_template_code = sm_template_code
        self.code_len = code_len
        self._content_type = "application/x-www-form-urlencoded;charset=utf-8"
        self._send_sm_base_url = "https://api.netease.im/sms/sendcode.action"
        self._verify_sm_base_url = "https://api.netease.im/sms/verifycode.action"

    def send_sm_code(self) -> str:
        """
        发送验证码
        :return:
        """
        cur_time, nonce, check_sum = self._build_check_args()
        request_headers = {
            "Content-Type": self._content_type,
            "AppKey": self.app_key,
            "CurTime": cur_time,
            "Nonce": nonce,
            "CheckSum": check_sum,
        }
        try:
            res = requests.post(
                url=self._send_sm_base_url,
                headers=request_headers,
                data={"mobile": self.mobile, "templateid": self.sm_template_code, "codeLen": self.code_len},
                timeout=5
            )
        except Exception as e:
            traceback.print_exc()
            return ""
        return res.json()

    def verity_sm_code(self, code: str) -> str:
        """
        校验验证码
        :param code: 验证码
        :return:
        """
        cur_time, nonce, check_sum = self._build_check_args()
        request_headers = {
            "Content-Type": self._content_type,
            "AppKey": self.app_key,
            "CurTime": cur_time,
            "Nonce": nonce,
            "CheckSum": check_sum,
        }
        try:
            res = requests.post(
                url=self._verify_sm_base_url,
                headers=request_headers,
                data={"mobile": self.mobile, "code": code},
                timeout=5
            )
        except Exception as e:
            traceback.print_exc()
            return ""
        return res.json()

    def _build_check_args(self):
        """
        构建使用参数
        :return:
        """
        cur_time = str(int(time.time()))
        nonce = str(random.randint(0, 10))
        temp_str = self.app_secret + nonce + cur_time
        check_sum = hashlib.sha1(temp_str.encode("utf-8")).hexdigest()
        return cur_time, nonce, check_sum


if __name__ == '__main__':
    sm = SmService("你的手机号", "你的appkey", "app_secret", "短信模板id,[数字类型]")
    print(sm.verity_sm_code("你的验证码"))
