#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_qjd
Author: Curtin
功能：全民抢京豆（7.2-7.15）：https://h5.m.jd.com/rn/3MQXMdRUTeat9xqBSZDSCCAE9Eqz/index.html?has_native=0
    满160豆需要20人助力，每个用户目前只能助力2次不同的用户。
Date: 2021/7/3 上午10:02
TG交流 https://t.me/topstyle996
TG频道 https://t.me/TopStyle2021
update: 2021.7.6 00:34
* 修复了助力活动不存在、增加了随机UA（如果未定义ua则启用随机UA）
* 新增推送
* 修复0点不能开团
'''

#ck 优先读取【JDCookies.txt】 文件内的ck  再到 ENV的 变量 JD_COOKIE='ck1&ck2' 最后才到脚本内 cookies=ck

cookies = 'pt_key=AAJhCnlJADD5XbTbLRdbc0ICWVPu-3z-dG8wnJ9UpJrqMzELeo3vUvdstyer-pt3_aaQ4eb4hn4;pt_pin=jd_ZTxRgzutYoug;& pt_key=AAJg7v4lADCpfHxW0wfSsVapQfFGMV8tYfo3NB2kMhwTLXRuJTT1Chbxtl8ROrIgKL76-uplcuc;pt_pin=%E5%8C%97%E4%BA%AC%E4%B8%AD%E5%8C%BB%E8%8D%AF;&pt_key=AAJhCnZVADCuDrq5YwzAaO47S1BLJ6I7uh5YZ5Rbjz7XLAKut_fiN3QyyOflezXnlLTu-LEWdiE;pt_pin=jd_5134684b1dd8c;&pt_key=AAJhC-GkADBmmYBSwIJHVsY4-3YmetS51SESXau9Q_hTiRP9gFmpfpPnQLwObByr-5l-pyQtPh8;pt_pin=jd_44eb8e75150b0;&pt_key=AAJhC6dVADANEQW4mZ-xxkmgGAPmXx0VdQ1yRfSClGql36XZ25wveNRlK4FFGfAnUtueBfR2r-c;pt_pin=jd_cLmIBPqnwcbZ;&pt_key=AAJhC6hTADAouqXTZoy2F3efMg661jlB1i7IkDxHrzFAVrHHLtoPV_7vBVxxJo7YmMdStqYTnAs;pt_pin=jd_495f1d13eb5f3;&pt_key=AAJhC98jADAD_zRUSsmj6U5Whf5sKOsyytcCT2-VSCpYRS5NtFg7B7Ifa7zc4KbYCSR8SWds-qw;pt_pin=jd_75bb875516cac;&pt_key=AAJhC-KoADDARXsaPLFOlgG-i5R79wDXcvv61o8MS8IgTWc2tNinSo_PeTwU9DQLpPiWqtptCTY;pt_pin=1289795742_m;&pt_key=AAJhC8c3ADD0wKttlcrxVMxic4epNQzWYN-tQj3rUlPSJ-YauEbyEmgOC9ZDRIjEl-BuUkH58fo;pt_pin=hg1003090227;&pt_key=AAJhC8eRADBBeBD0ppRlJ2a_ZOspnw49icG7Rh9z5ILyfqJrmjnw0OR1zqI_e73l9bRd6K9skbk;pt_pin=jd_56efbbcd0c007;&pt_key=AAJhC8gjADBB_6aR-aI5AnGRcBeL-SYi5AHzkGymCxMW_VJ5NbbbmChE8JxKYHP-Jx9x-ut2qpY;pt_pin=jd_zJdrpMzszadm;&pt_key=AAJhC92HADAGhMw4kj1m0NYEDa03gXLoDC38UqCnKA5GrZFo1u4dq6AASR9GHD7uiiGOJ8YOxPQ;pt_pin=s1690582662848220;&pt_key=AAJhC-NlADDE9apsP4AByYfbf3JE_aSMxY1g9vgEEwW7Gl4alMzIKYtu1iReINh1fWSdJy-SM4M;pt_pin=yalhu;&pt_key=AAJhC_m2AEBwzYp-EG5_Dj_DqfyB80FeFTacSvOi-5CqJu1DmpTCo36HkbeEJG-_cYvc1YGZgATfu7n51XEKyYs5JVeGNnoI;pt_pin=%E6%B7%A1%E7%B4%AB%E8%89%B2%E7%9A%84%E9%AD%85%E5%8A%9B;&pt_key=AAJhC8fjADBS-27t-WLA-Csd_5pTuaC7AUfb2Ltko06LdboBwVB7nQn998dKhPT-fzESk9I4ZMw;pt_pin=jd_cxtuOOSClYNb;&pt_key=AAJhC6tLADBfO-beBtwq8F2gtlHk8yOqrn6uLm2O-I55WRPwvy-OBy5UE1Ac_5bwWU5LiRqOlYM;pt_pin=jd_693990a8889b7;&pt_key=AAJhC93tADCXNb1g4QaqJz_cfuuBdzGW7fsansvRBPcwxkbeX5fNwif3fWM3n4SYDua_8y37PA0;pt_pin=%E6%A8%97%E9%9B%A9;&pt_key=AAJhDURjADBAGlfa7XCoPmcQAiW3tzouwaRyH3RpS2iGTEWWHa2iQJYq_Hk9V7qTdip2aol9zLI;pt_pin=wdZmWwCsNZeEty;&pt_key=AAJhC-QGADCrr3KU4Nn_9QvftgNakp-IWemsWc45TARTUlSfsfzxF6hzC_JuZsb-__RTpP0hujA;pt_pin=59589922-696704;&pt_key=AAJhC-cUADCMUuoYZC-MOtfQRd2rQBYzH0eHkyVf9zx1Rwye8XxvUU8hTRrQOl4MrYrR8dAkbMQ;pt_pin=%E8%8D%9E%E9%BA%A6bb;&pt_key=AAJhC-yoADDx4TdhKSi8nOkVMXvLd_UCX7m5YxDql6xlVilWGFKm0s6VP0axe6SLzaYJQe2iv74;pt_pin=107%E6%B7%A1%E7%84%B6;&pt_key=AAJhC-2kADB_ktdGiQB_v1YHHCZW8el5yiHHrqVA9LLr7ijo9e4Mfzqy5DJx9wzDSD94BjGXPBg;pt_pin=1371298353_m;&pt_key=AAJhC6xMADANxq-SQzIL1_YEE1zfcBvS29NKZkQjnmiuQbYTA3ScAeRMWs4yalILmYNK-vs9znc;pt_pin=warage_m;&pt_key=AAJhDme1ADCtD7GsZqrdjglBarW_oqQFV6BnyFALpM9i0tddmkPHJQtP7MfgziPEsE5qD2yjboI;pt_pin=jd_7f735d89664e6;&pt_key=AAJhDl50ADB9xMM76le7lYX2poPBOS_RnJadOR0REO9NmWbtMi32CQcHetg6j6oF1AyuZ2shnnQ;pt_pin=%E6%B8%85%E6%9E%AB%E6%B5%81%E5%B9%B4;&pt_key=AAJg7CegADCg2VG8aZ4dg6_QZAM_FQEojV9lhoxEY-3WcQqBfcGDOjyS5kDP4zHzcpapeMj7fCs;pt_pin=lanyu27;&pt_key=AAJhDiadADCg9oaV4oAAsitKtR4Jg3ytx9WhbF66V8vLtD_ZxNJwJy8SSMs58gku-BHzwrjfEXc;pt_pin=wdTNhojwXsNCrq;&pt_key=AAJg7CgMADDWM5zJQdFAGtU-gFK_JKhk3hquPQL6IhgZD4fVVjc_CgD8LHqSe4a5keeZh7ylzSA;pt_pin=jiajingyou001;&pt_key=AAJg7C3VAEDkeAw9h8yKYJ3-KVTImbNC9RZB62B6-BHSgTqkhomJ1Yybs8MfjvgL01hPDtZBWDr-cMCH4xIFxp-JnIijrXJl;pt_pin=%E5%B0%8F%E7%9A%AE%E5%93%A9%E5%92%95%E5%93%A9%E5%92%95;&pt_key=AAJg7EQ9ADAD0OvqqfjF_ltC5H44BliL_1LsopKIvOFqQMAj6Zh3WHz-i_FFdqqpxKfymMDOR54;pt_pin=jd_76cbed94c22ae;&pt_key=AAJg7Xr1ADBshp-imSWl3Gb61goDGxttR-YFQsEk12oQNjV7BxYcXhQguttwDiyhzShPdM3GBT0;pt_pin=jd_4a38c7a8ca424;&pt_key=AAJhDl7cADBFqGAapN0tpuWAeSWHQBTVUMcAyPl95Z4lSNVTcZof2Wi8EJY7cgSFE7WX2kUErFI;pt_pin=jd_dNaavvwAeubq;&pt_key=AAJhDl90ADAkjakWk0c4KsSk8nssjOYzqrHW3doNnmSJg5frTxoHJdaN-Ke3ZK0W-dTmcOmAmec;pt_pin=jd_ONosmyTkCpDQ;&pt_key=AAJg8D8vADB9yhQS7p7dx_3eENrVTbSC2UMfAPqqxygI3DDGVF-rzH8_xoTPZ7A6xumqEnhpqyY;pt_pin=%E5%BC%A0%E7%AC%915210;'
qjd_zlzh = ['jd大备语', '柠檬葡萄汽水汁', '大咩929']

# Env环境设置 通知服务
# export BARK=''                   # bark服务,苹果商店自行搜索;
# export SCKEY=''                  # Server酱的SCKEY;
# export TG_BOT_TOKEN=''           # tg机器人的TG_BOT_TOKEN;
# export TG_USER_ID=''             # tg机器人的TG_USER_ID;
# export TG_API_HOST=''            # tg 代理api
# export TG_PROXY_IP=''            # tg机器人的TG_PROXY_IP;
# export TG_PROXY_PORT=''          # tg机器人的TG_PROXY_PORT;
# export DD_BOT_ACCESS_TOKEN=''    # 钉钉机器人的DD_BOT_ACCESS_TOKEN;
# export DD_BOT_SECRET=''          # 钉钉机器人的DD_BOT_SECRET;
# export QQ_SKEY=''                # qq机器人的QQ_SKEY;
# export QQ_MODE=''                # qq机器人的QQ_MODE;
# export QYWX_AM=''                # 企业微信；http://note.youdao.com/s/HMiudGkb
# export PUSH_PLUS_TOKEN=''        # 微信推送Plus+ ；

#####

# 建议调整一下的参数
# UA 可自定义你的，注意格式: jdapp;iPhone;10.0.4;13.1.1;93b4243eeb1af72d142991d85cba75c66873dca5;network/wifi;ADID/8679C062-A41A-4A25-88F1-50A7A3EEF34A;model/iPhone13,1;addressid/3723896896;appBuild/167707;jdSupportDarkMode/0
UserAgent = ''
# 限制速度 （秒）
sleepNum = 0.1

import os, re, sys
import random, string
try:
    import requests
except Exception as e:
    print(e, "\n缺少requests 模块，请执行命令安装：python3 -m pip install requests")
    exit(3)
from urllib.parse import unquote
import json
import time
requests.packages.urllib3.disable_warnings()

pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep
t = time.time()
aNum = 0
beanCount = 0
userCount = {}

######## 获取通知模块
message_info = ''''''
def message(str_msg):
    global message_info
    print(str_msg)
    message_info = "{}\n{}".format(message_info, str_msg)
    sys.stdout.flush()
def getsendNotify(a=0):
    if a == 0:
        a += 1
    try:
        url = 'https://gitee.com/curtinlv/Public/raw/master/sendNotify.py'
        response = requests.get(url)
        if 'main' in response.text:
            with open('sendNotify.py', "w+", encoding="utf-8") as f:
                f.write(response.text)
        else:
            if a < 5:
                a += 1
                return getsendNotify(a)
            else:
                pass
    except:
        if a < 5:
            a += 1
            return getsendNotify(a)
        else:
            pass
cur_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(cur_path)
if os.path.exists(cur_path + "/sendNotify.py"):
    from sendNotify import send
else:
    getsendNotify()
    try:
        from sendNotify import send
    except:
        print("加载通知服务失败~")
###################

###### 获取cookie
class getJDCookie(object):
    # 适配各种平台环境ck
    def getckfile(self):
        if os.path.exists(pwd + 'JDCookies.txt'):
            return pwd + 'JDCookies.txt'
        elif os.path.exists('/ql/config/env.sh'):
            print("当前环境青龙面板新版")
            return '/ql/config/env.sh'
        elif os.path.exists('/ql/config/cookie.sh'):
            print("当前环境青龙面板旧版")
            return '/ql/config/env.sh'
        elif os.path.exists('/jd/config/config.sh'):
            print("当前环境V4")
            return '/jd/config/config.sh'
        elif os.path.exists(pwd + 'JDCookies.txt'):
            return pwd + 'JDCookies.txt'
        return pwd + 'JDCookies.txt'

    # 获取cookie
    def getCookie(self):
        global cookies
        ckfile = self.getckfile()
        try:
            if os.path.exists(ckfile):
                with open(ckfile, "r", encoding="utf-8") as f:
                    cks = f.read()
                    f.close()
                if 'pt_key=' in cks and 'pt_pin=' in cks:
                    r = re.compile(r"pt_key=.*?pt_pin=.*?;", re.M | re.S | re.I)
                    cks = r.findall(cks)
                    if len(cks) > 0:
                        if 'JDCookies.txt' in ckfile:
                            print("当前获取使用 JDCookies.txt 的cookie")
                        cookies = ''
                        for i in cks:
                            cookies += i
                        return
            else:
                with open(pwd + 'JDCookies.txt', "w", encoding="utf-8") as f:
                    cks = "#多账号换行，以下示例：（通过正则获取此文件的ck，理论上可以自定义名字标记ck，也可以随意摆放ck）\n账号1【Curtinlv】cookie1;\n账号2【TopStyle】cookie2;"
                    f.write(cks)
                    f.close()
            if "JD_COOKIE" in os.environ:
                if len(os.environ["JD_COOKIE"]) > 10:
                    cookies = os.environ["JD_COOKIE"]
                    print("已获取并使用Env环境 Cookie")
        except Exception as e:
            print(f"【getCookie Error】{e}")

    # 检测cookie格式是否正确
    def getUserInfo(self, ck, pinName, userNum):
        url = 'https://me-api.jd.com/user_new/info/GetJDUserInfoUnion?orgFlag=JD_PinGou_New&callSource=mainorder&channel=4&isHomewhite=0&sceneval=2&sceneval=2&callback=GetJDUserInfoUnion'
        headers = {
            'Cookie': ck,
            'Accept': '*/*',
            'Connection': 'close',
            'Referer': 'https://home.m.jd.com/myJd/home.action',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'me-api.jd.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1',
            'Accept-Language': 'zh-cn'
        }
        try:
            resp = requests.get(url=url, verify=False, headers=headers, timeout=60).text
            r = re.compile(r'GetJDUserInfoUnion.*?\((.*?)\)')
            result = r.findall(resp)
            userInfo = json.loads(result[0])
            nickname = userInfo['data']['userInfo']['baseInfo']['nickname']
            return ck, nickname
        except Exception:
            context = f"账号{userNum}【{pinName}】Cookie 已失效！请重新获取。"
            print(context)
            return ck, False

    def iscookie(self):
        """
        :return: cookiesList,userNameList,pinNameList
        """
        cookiesList = []
        userNameList = []
        pinNameList = []
        if 'pt_key=' in cookies and 'pt_pin=' in cookies:
            r = re.compile(r"pt_key=.*?pt_pin=.*?;", re.M | re.S | re.I)
            result = r.findall(cookies)
            if len(result) >= 1:
                print("您已配置{}个账号".format(len(result)))
                u = 1
                for i in result:
                    r = re.compile(r"pt_pin=(.*?);")
                    pinName = r.findall(i)
                    pinName = unquote(pinName[0])
                    # 获取账号名
                    ck, nickname = self.getUserInfo(i, pinName, u)
                    if nickname != False:
                        cookiesList.append(ck)
                        userNameList.append(nickname)
                        pinNameList.append(pinName)
                    else:
                        u += 1
                        continue
                    u += 1
                if len(cookiesList) > 0 and len(userNameList) > 0:
                    return cookiesList, userNameList, pinNameList
                else:
                    print("没有可用Cookie，已退出")
                    exit(3)
            else:
                print("cookie 格式错误！...本次操作已退出")
                exit(4)
        else:
            print("cookie 格式错误！...本次操作已退出")
            exit(4)
getCk = getJDCookie()
getCk.getCookie()

if "qjd_zlzh" in os.environ:
    if len(os.environ["qjd_zlzh"]) > 1:
        qjd_zlzh = os.environ["qjd_zlzh"]
        qjd_zlzh = qjd_zlzh.replace('[', '').replace(']', '').replace('\'', '').replace(' ', '').split(',')
        print("已获取并使用Env环境 qjd_zlzh:", qjd_zlzh)

def userAgent():
    """
    随机生成一个UA
    :return:
    """
    if not UserAgent:
        uuid = ''.join(random.sample('123456789abcdef123456789abcdef123456789abcdef123456789abcdef', 40))
        iosVer = ''.join(random.sample(["14.5.1", "14.4", "14.3", "14.2", "14.1", "14.0.1", "13.7", "13.1.2", "13.1.1"], 1))
        iPhone = ''.join(random.sample(["8", "9", "10", "11", "12", "13"], 1))
        return f'jdapp;iPhone;10.0.4;{iosVer};{uuid};network/wifi;ADID/8679C062-A41A-4A25-88F1-50A7A3EEF34A;model/iPhone{iPhone},1;addressid/3723896896;appBuild/167707;jdSupportDarkMode/0'
    else:
        return UserAgent

def getShareCode(ck):
    global aNum
    try:
        # uuid = ''.join(random.sample('123456789abcdef123456789abcdef123456789abcdef123456789abcdef', 40))
        v_num1 = ''.join(random.sample(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 1)) + ''.join(random.sample(string.digits, 4))
        url1 = f'https://api.m.jd.com/client.action?functionId=signGroupHit&body=%7B%22activeType%22%3A2%7D&appid=ld&client=apple&clientVersion=10.0.6&networkType=wifi&osVersion=14.3&uuid=&jsonp=jsonp_' + str(int(round(t * 1000))) + '_' + v_num1
        url = 'https://api.m.jd.com/client.action?functionId=signBeanGroupStageIndex&body=%7B%22monitor_refer%22%3A%22%22%2C%22rnVersion%22%3A%223.9%22%2C%22fp%22%3A%22-1%22%2C%22shshshfp%22%3A%22-1%22%2C%22shshshfpa%22%3A%22-1%22%2C%22referUrl%22%3A%22-1%22%2C%22userAgent%22%3A%22-1%22%2C%22jda%22%3A%22-1%22%2C%22monitor_source%22%3A%22bean_m_bean_index%22%7D&appid=ld&client=apple&clientVersion=&networkType=&osVersion=&uuid=&jsonp=jsonp_' + str(int(round(t * 1000))) + '_' + v_num1
        head = {
            'Cookie': ck,
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Referer': 'https://h5.m.jd.com/rn/3MQXMdRUTeat9xqBSZDSCCAE9Eqz/index.html?has_native=0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'api.m.jd.com',
            # 'User-Agent': 'Mozilla/5.0 (iPhone CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1',
            'User-Agent': userAgent(),
            'Accept-Language': 'zh-cn'
        }
        requests.get(url1,  headers=head, verify=False, timeout=30)
        resp = requests.get(url=url, headers=head, verify=False, timeout=30).text
        r = re.compile(r'jsonp_.*?\((.*?)\)\;', re.M | re.S | re.I)
        result = r.findall(resp)
        jsonp = json.loads(result[0])
        try:
            groupCode = jsonp['data']['groupCode']
            shareCode = jsonp['data']['shareCode']
            activityId = jsonp['data']['activityMsg']['activityId']
            sumBeanNumStr = int(jsonp['data']['sumBeanNumStr'])
        except:
            if aNum < 5:
                aNum += 1
                return getShareCode(ck)
            else:
                groupCode = 0
                shareCode = 0
                sumBeanNumStr = 0
                aNum = 0
                activityId = 0
        aNum = 0
        return groupCode, shareCode, sumBeanNumStr, activityId
    except Exception as e:
        print(f"getShareCode Error", e)

def helpCode(ck, groupCode, shareCode,u, unum, user, activityId):
    try:
        v_num1 = ''.join(random.sample(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 1)) + ''.join(random.sample(string.digits, 4))
        headers = {
            'Cookie': ck,
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Referer': f'https://h5.m.jd.com/rn/42yjy8na6pFsq1cx9MJQ5aTgu3kX/index.html?jklActivityId=115&source=SignSuccess&jklGroupCode={groupCode}&ad_od=1&jklShareCode={shareCode}',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'api.m.jd.com',
            'User-Agent': userAgent(),
            'Accept-Language': 'zh-cn'
        }
        url = 'https://api.m.jd.com/client.action?functionId=signGroupHelp&body=%7B%22activeType%22%3A2%2C%22groupCode%22%3A%22' + str(groupCode) + '%22%2C%22shareCode%22%3A%22' + shareCode + f'%22%2C%22activeId%22%3A%22{activityId}%22%2C%22source%22%3A%22guest%22%7D&appid=ld&client=apple&clientVersion=10.0.4&networkType=wifi&osVersion=13.7&uuid=&openudid=&jsonp=jsonp_{int(round(t * 1000))}_{v_num1}'
        resp = requests.get(url=url, headers=headers, verify=False, timeout=30).text
        r = re.compile(r'jsonp_.*?\((.*?)\)\;', re.M | re.S | re.I)
        result = r.findall(resp)
        jsonp = json.loads(result[0])
        helpToast = jsonp['data']['helpToast']
        pageFlag = jsonp['data']['pageFlag']
        if pageFlag == 0:
            print(f"账号{unum}【{u}】助力失败! 原因：{helpToast}")
            if '满' in helpToast:
                print(f"## 恭喜账号【{user}】团已满，今日累计获得160豆")
                return True
            return False
        else:
            if '火' in helpToast:
                print(f"账号{unum}【{u}】助力失败! 原因：{helpToast}")
            else:
                print(f"账号{unum}【{u}】{helpToast} , 您也获得1豆哦~")
            return False
    except Exception as e:
        print(f"helpCode Error ", e)

def start():
    scriptName='### 全民抢京豆-助力 ###'
    print(scriptName)
    global cookiesList, userNameList, pinNameList, ckNum, beanCount, userCount
    cookiesList, userNameList, pinNameList = getCk.iscookie()
    for ckname in qjd_zlzh:
        try:
            ckNum = userNameList.index(ckname)
        except Exception as e:
            try:
                ckNum = pinNameList.index(ckname)
            except:
                print(f"请检查被助力账号【{ckname}】名称是否正确？提示：助力名字可填pt_pin的值、也可以填账号名。")
                continue

        print(f"### 开始助力账号【{userNameList[int(ckNum)]}】###")
        groupCode, shareCode, sumBeanNumStr, activityId = getShareCode(cookiesList[ckNum])
        if groupCode == 0:
            message(f"## {userNameList[int(ckNum)]}  获取互助码失败。请手动分享后再试~ 或建议早上再跑。")
            continue
        u = 0
        for i in cookiesList:
            if i == cookiesList[ckNum]:
                u += 1
                continue
            result = helpCode(i, groupCode, shareCode, userNameList[u], u+1, userNameList[int(ckNum)], activityId)
            time.sleep(sleepNum)
            if result:
                break
            u += 1
        groupCode, shareCode, sumBeanNumStr, activityId = getShareCode(cookiesList[ckNum])
        userCount[f'{userNameList[ckNum]}'] = sumBeanNumStr
        beanCount += sumBeanNumStr
    print("\n-------------------------")
    for i in userCount.keys():
        message(f"账号【{i}】已抢京豆: {userCount[i]}")
    message(f"## 今日累计获得 {beanCount} 京豆")
    try:
        send(scriptName, message_info)
    except:
        pass


if __name__ == '__main__':
    start()
