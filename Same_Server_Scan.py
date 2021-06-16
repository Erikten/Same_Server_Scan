# -*- coding: gbk -*-
# @Time    : 2021/6/16 11:03
# @Author  : Erikten
# @Site    :
# @File    : Same_Server_Scan.py
# @Software: PyCharm

import requests
import json


def querySite(data,page,url):

    with open(f'{url}.txt', 'a+') as f:
        f.write('-' * 20 + f'第 {page} 页' + '-' * 20 + '\n\n')

    new_data = data['data']
    for i in new_data['domains']:
        # print("域名 : %s \n网站标题 : %s \n爱站PC权重 : %s \n爱站移动权重 : %s \n搜狗权重 : %s\n谷歌权重 : %s\n" %(i['domain'], i['title'], i['pc_br'], i['m_br'], i['sogou_pr'], i['google_pr']))
        res = "\t域名 : %s \n\t网站标题 : %s \n\t爱站PC权重 : %s \n\t爱站移动权重 : %s \n\t搜狗权重 : %s\n\t谷歌权重 : %s\n\n" % (
            i['domain'], i['title'], i['pc_br'], i['m_br'], i['sogou_pr'], i['google_pr'])

        with open(f'{url}.txt', 'a+') as f:
            f.write(res)

    with open(f'{url}.txt', 'a+') as f:
        f.write('-' * 20 + f'第 {page} 页' + '-' * 20 + '\n\n')
    print(f'第 {page} 页的结果已输出到 {url}.txt ,请注意查收 !\n')
    try:
        chose = input('是否继续收集下一页结果 ? ( y )') or 'y'
        if chose == 'y':
            page = int(page)+1
            global key
            api = 'https://apistore.aizhan.com/site/dnsinfos/'+key+'?query='+url+'&page=%d'%page
            html = requests.get(url=api).text
            data = json.loads(html)
            reqStatus(data, page, url)
        elif page == 'n':
            exit('感谢使用, 期待下次再会 ~')
        else:
            exit('感谢使用, 期待下次再会 ~')
    except:
        print('感谢使用, 期待下次再会 ~')

def reqStatus(data,page,url):

    if data['code'] == 200000:

        new_data = data['data']
        info = f"\n主站 : {new_data['query']}\nIP地址 : {new_data['ip']}\nIP地区 : {new_data['address']}\n总条数 : {new_data['total_num']}\n总页数 : {new_data['total_pages']}\n当前页数 : {new_data['current_page']}\n"
        print(info)

        with open(f'{url}.txt', 'a+') as f:
            f.write(info + '\n')
        querySite(data,page,url)

    elif data['code'] == 200001:
        print('参数错误 !')

    elif data['code'] == 200005:
        print('数据错误,请重试 !')

    elif data['code'] == 200006:
        print('暂无数据 !')

    elif data['code'] == 100000:
        print('未知错误 !')

    elif data['code'] == 100001:
        print('缺少hash !')

    elif data['code'] == 100002:
        print('无效hash !')

    elif data['code'] == 100003:
        print('接口维护 !')

    elif data['code'] == 100004:
        print('接口停用 !')

    elif data['code'] == 100005:
        print('余额不足,请充值 !')

    elif data['code'] == 100005:
        print('支付失败,请重试 !')

    else:
        print('您的操作太牛了, 程序已飞走...')

def reqSite(key,url,page=1):
    api = 'https://apistore.aizhan.com/site/dnsinfos/'+key+'?query='+url+'&page=%d'%page
    html = requests.get(url=api).text
    data = json.loads(html)
    reqStatus(data, page, url)


if __name__ == '__main__':
    print(''' __                          __                           __                 
/ _\ __ _ _ __ ___   ___    / _\ ___ _ ____   _____ _ __ / _\ ___ __ _ _ __  
\ \ / _` | '_ ` _ \ / _ \   \ \ / _ \ '__\ \ / / _ \ '__|\ \ / __/ _` | '_ \ 
_\ \ (_| | | | | | |  __/   _\ \  __/ |   \ V /  __/ |   _\ \ (_| (_| | | | |
\__/\__,_|_| |_| |_|\___|___\__/\___|_|    \_/ \___|_|___\__/\___\__,_|_| |_|
                       |_____|                      |_____|                           v 1.0         
    ''')



    # js = '{"code":200000,"status":"success","data":{"query":"www.aizhan.com","ip":"125.77.130.22","address":"\u798f\u5efa\u6cc9\u5dde \u7535\u4fe1","total_num":1261,"total_pages":64,"current_page":1,"domains":[{"domain":"www.28.com","title":"28\u5546\u673a\u7f51&amp;mdash;&amp;mdash;\u62db\u5546\u52a0\u76df\u884c\u4e1a\u7f8e\u56fd\u4e0a\u5e02\u54c1\u724c(\u627e\u8fde\u9501\u521b\u4e1a\u9879\u76ee)","pc_br":2,"m_br":1,"sogou_pr":0,"google_pr":5},{"domain":"www.4008898188.com","title":"\u9c9c\u82b1\u7f51|\u82b1\u793c\u7f51-\u4e2d\u56fd\u9c9c\u82b1\u793c\u54c1\u7f51,\u9c9c\u82b1\u901f\u9012\u7f51\u7ad9,\u7f51\u4e0a\u8ba2\u82b1\u9001\u82b1\u4e0a\u95e8,\u540c\u57ce\u9c9c\u82b1\u5feb\u9012\u7f51\u4e0a\u82b1\u5e97","pc_br":0,"m_br":0,"sogou_pr":0,"google_pr":0},{"domain":"www.52edy.com","title":"\u8349\u56fe\u5927\u5e08\u6a21\u578b sketchup\u6a21\u578b\u4e0b\u8f7d sketchup\u6a21\u578b\u514d\u8d39\u4e0b\u8f7d SU\u6a21\u578b\u4e0b\u8f7d","pc_br":3,"m_br":1,"sogou_pr":0,"google_pr":0},{"domain":"www.7xdown.com","title":"\u4e03\u559c\u4e0b\u8f7d\u7ad9_\u5b98\u65b9\u8f6f\u4ef6\u4e0b\u8f7d_\u7eff\u8272\u8f6f\u4ef6_\u6e38\u620f\u4e0b\u8f7d_\u6700\u5b89\u5168\u7684\u4e0b\u8f7d\u7ad9","pc_br":5,"m_br":0,"sogou_pr":0,"google_pr":5},{"domain":"www.arswp.com","title":"Windows\u6e05\u7406\u52a9\u624b","pc_br":2,"m_br":1,"sogou_pr":0,"google_pr":5},{"domain":"www.asianewsphoto.com","title":"Asia News Photo","pc_br":0,"m_br":0,"sogou_pr":0,"google_pr":6},{"domain":"www.cnd8.com","title":"\u624b\u673a\u6e38\u620f\u6392\u884c\u699c_\u6700\u706b\u597d\u73a9\u624b\u673a\u6e38\u620f\u6392\u884c\u699c\u524d\u5341\u540d_\u83dc\u9e1f\u6e38\u620f\u7f51","pc_br":3,"m_br":3,"sogou_pr":0,"google_pr":6},{"domain":"www.cnmo.com","title":"CNMO-\u4e13\u4e1a.\u6709\u8da3\u7684\u79d1\u6280\u65b0\u5a92\u4f53","pc_br":5,"m_br":4,"sogou_pr":0,"google_pr":7},{"domain":"www.cy.com","title":"\u7545\u6e38-ChangYou.com","pc_br":0,"m_br":0,"sogou_pr":0,"google_pr":1},{"domain":"www.danji8.com","title":"\u5355\u673a8\u4e0b\u8f7d\u7ad9-\u8f6f\u4ef6\u4e0b\u8f7d-\u6e38\u620f\u4e0b\u8f7d","pc_br":0,"m_br":0,"sogou_pr":0,"google_pr":3},{"domain":"www.ddooo.com","title":"\u591a\u591a\u8f6f\u4ef6\u7ad9-\u63d0\u4f9b\u7eff\u8272\u8f6f\u4ef6\u548c\u70ed\u95e8\u5355\u673a\u6e38\u620f\u4e0b\u8f7d","pc_br":7,"m_br":2,"sogou_pr":0,"google_pr":6},{"domain":"www.eastmoney.com","title":"\u4e1c\u65b9\u8d22\u5bcc\u7f51\uff1a\u8d22\u7ecf\u95e8\u6237\uff0c\u63d0\u4f9b\u4e13\u4e1a\u7684\u8d22\u7ecf\u3001\u80a1\u7968\u3001\u884c\u60c5\u3001\u8bc1\u5238\u3001\u57fa\u91d1\u3001\u7406\u8d22\u3001\u94f6\u884c\u3001\u4fdd\u9669\u3001\u4fe1\u6258\u3001\u671f\u8d27\u3001\u9ec4\u91d1\u3001\u80a1\u5427\u3001\u535a\u5ba2\u7b49\u5404\u7c7b\u8d22\u7ecf\u8d44\u8baf\u53ca\u6570\u636e","pc_br":6,"m_br":2,"sogou_pr":0,"google_pr":7},{"domain":"www.fia-china.com","title":"Hi &amp; Fi Asia-China \u5065\u5eb7\u539f\u6599\uff0c\u98df\u54c1\u914d\u6599\u4e2d\u56fd\u5c55 | \u98df\u54c1\u6dfb\u52a0\u5242\u5c55 |FIC","pc_br":0,"m_br":0,"sogou_pr":0,"google_pr":4},{"domain":"www.hunantv.com","title":"\u58f0\u660e\u516c\u544a_\u6e56\u5357\u5feb\u4e50\u9633\u5149\u4e92\u52a8\u5a31\u4e50\u4f20\u5a92\u6709\u9650\u516c\u53f8","pc_br":5,"m_br":6,"sogou_pr":0,"google_pr":7},{"domain":"www.ifeng.com","title":"\u51e4\u51f0\u7f51","pc_br":5,"m_br":2,"sogou_pr":0,"google_pr":8},{"domain":"www.kingsoft.com","title":"\u91d1\u5c71\u5728\u7ebf - \u505a\u4e16\u754c\u4e00\u6d41\u7684\u8f6f\u4ef6\u4f01\u4e1a","pc_br":3,"m_br":1,"sogou_pr":0,"google_pr":7},{"domain":"www.m1905.com","title":"\u7535\u5f71\u7f51_1905.com","pc_br":4,"m_br":3,"sogou_pr":0,"google_pr":7},{"domain":"www.mamecn.com","title":"\u8857\u673a\u6e38\u620f_\u8857\u673a\u6e38\u620f\u4e0b\u8f7d_\u8857\u673a\u6a21\u62df\u5668\u6e38\u620f\u4e0b\u8f7d-\u8857\u673a\u4e2d\u56fd","pc_br":5,"m_br":1,"sogou_pr":0,"google_pr":5},{"domain":"www.mop.com","title":"\u732b\u6251-\u732b\u6251\u7f51","pc_br":4,"m_br":1,"sogou_pr":0,"google_pr":7},{"domain":"www.myswitzerland.com","title":"Switzerland Travel &amp; Vacation | Switzerland Tourism","pc_br":1,"m_br":1,"sogou_pr":0,"google_pr":8}]},"msg":"\u8bf7\u6c42\u6210\u529f"}'

    key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"        # 爱站API市场账号私钥  https://www.aizhan.com/apistore/

    url = input('请输入要查询的域名: ')
    if 'http' in url:
        url = url.split('http://')[1]
    elif 'https' in url:
        url = url.split('https://')[1]

    reqSite(key, url,)