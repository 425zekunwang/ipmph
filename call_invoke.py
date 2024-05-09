import concurrent.futures
import json
import time
import traceback

import tqdm
from lxml import etree
import requests
import re
from concurrent.futures.thread import ThreadPoolExecutor
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-type": "application/x-www-form-urlencoded",
    "Cookie": "JSESSIONID=62D9ABFE6F4BE1B0F9BDC01EEA8DC794; UniqueID=tXVvDg8wtzcRYHDU1714987500016; Sites=_0; route=6956ef56584808585a187954e8100680; __root_domain_v=.ipmph.com; _qddaz=QD.117814985994423; Hm_lvt_ec31b23a3a54fb0e85df69fc93bd5de9=1715133669; Hm_lpvt_ec31b23a3a54fb0e85df69fc93bd5de9=1715133669; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218f4d38f5b7190d-084705f8463bb28-4c657b58-1327104-18f4d38f5b8ab6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%AB%99%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%7D%2C%22identities%22%3A%22%5Cn%2F1vqr%7B%5Cu0003v%5Cu0003%5Cbln%7B%7C%7B%5Cbz%7C%5Cu0004%5Cu0002lvq%2FG%2F%3EEsAq%40EsBoD%3EF%3Dq%3A%3DEAD%3DBsEAC%40oo%3FE%3AApCBDoBE%3A%3E%40%3FD%3E%3DA%3A%3EEsAq%40EsBoEnoC%2F9%2F1vqr%7B%5Cu0003v%5Cu0003%5Cblp%7C%7Cxvrlvq%2FG%2F%3EEsBC%3Dn%3FrDFnpD%3A%3D%40%3D%3FEop%40FFDBnA%3AApCBDoBE%3A%3E%40%3FD%3E%3DA%3A%3EEsBC%3Dn%3FrDnF%3DE%2F%5Cf%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218f4d38f5b58b4-0001e573ac901e574-4c657b58-1327104-18f4d38f5b61a1e%22%7D; _qddab=3-ml9d5r.lvxlm4ia; undefined_vq=122",
    "Origin": "https://medbooks.ipmph.com",
    "Pragma": "no-cache",
    "Referer": "https://medbooks.ipmph.com/medical/medbooks/browse/bookList.zhtml?resourceType=ReferenceBook",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    "sec-ch-ua": "Chromium;v=124, Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
}
url = "https://medbooks.ipmph.com/medical/ajax/invoke"
def get_data(idx):
    return {
        "_ZVING_METHOD": "com.zving.framework.ui.control.DataListUI.doWork",
        "_ZVING_DATA_FORMAT": "json",
        "_ZVING_DATA": json.dumps(
            {"_ZVING_METHOD": "Lecture.getLectureList", "_ZVING_SIZE": "100", "_ZVING_AUTOFILL": "true",
             "_ZVING_PAGE": True, "_ZVING_ID": "list1", "classCode": "", "classType": "6",
             "resourceType": "LectureBook",
             "_ZVING_TAGBODY": "&lt;tr&gt;&nbsp;&lt;td&nbsp;valign=&quot;top&quot;&nbsp;class=&quot;boder-bottom&quot;&gt;&nbsp;&lt;div&nbsp;class=&quot;bg_color&quot;&nbsp;style=&quot;padding-right:13px;&quot;&gt;&nbsp;&lt;table&nbsp;width=&quot;100%&quot;&nbsp;border=&quot;0&quot;&nbsp;cellspacing=&quot;0&quot;&nbsp;cellpadding=&quot;0&quot;&gt;&nbsp;&lt;tr&nbsp;align=&quot;left&quot;&gt;&nbsp;&lt;td&nbsp;width=&quot;128&quot;&nbsp;align=&quot;center&quot;&gt;&nbsp;&lt;table&nbsp;border=&quot;0&quot;&nbsp;cellpadding=&quot;0&quot;&nbsp;cellspacing=&quot;0&quot;&nbsp;class=&quot;lb_yy&quot;&gt;&nbsp;&lt;tbody&gt;&lt;tr&gt;&nbsp;&lt;td&nbsp;valign=&quot;middle&quot;&nbsp;align=&quot;center&quot;&nbsp;class=&quot;lb_photo3&quot;&gt;&nbsp;&lt;a&nbsp;href=&quot;detailLecture.zhtml?bookId=${ID}&amp;resourceType=${ContentType}&quot;&nbsp;target=&quot;_blank&quot;&gt;&lt;img&nbsp;src=&quot;../../img.zhtml?ISRC=${ISRC}&amp;Type=0&amp;TimeCode=${TimeStamp}&amp;ImgType=3&quot;&nbsp;class=&quot;resizeImage&quot;&nbsp;height=&quot;114&quot;&nbsp;onload=&quot;autoHeight4Img(this,91,114);&quot;&nbsp;onerror=&quot;this.src='../images/zwtp_min.jpg'&quot;&nbsp;/&gt;&lt;/a&gt;&nbsp;&lt;/td&gt;&nbsp;&lt;/tr&gt;&nbsp;&lt;/tbody&gt;&nbsp;&lt;/table&gt;&nbsp;&lt;/td&gt;&nbsp;&lt;td&nbsp;valign=&quot;top&quot;&gt;&nbsp;&lt;table&nbsp;width=&quot;98%&quot;&nbsp;border=&quot;0&quot;&nbsp;cellpadding=&quot;0&quot;&nbsp;cellspacing=&quot;0&quot;&nbsp;class=&quot;lb_yy2&quot;&nbsp;&gt;&nbsp;&lt;tr&gt;&nbsp;&lt;td&gt;&nbsp;&lt;p&gt;&nbsp;&lt;span&nbsp;class=&quot;w_span&quot;&gt;&nbsp;&lt;span&nbsp;class=&quot;jg_font_h21_bt1&quot;&gt;&lt;a&nbsp;href=&quot;detailLecture.zhtml?bookId=${ID}&amp;resourceType=${ContentType}&quot;&nbsp;target=&quot;_blank&quot;&nbsp;style=&quot;color:#FF6C00;&quot;&gt;${mainTitle}&lt;/a&gt;&lt;/span&gt;&nbsp;&lt;/span&gt;&nbsp;${HasPriv}&nbsp;&lt;/p&gt;&nbsp;&lt;span&nbsp;class=&quot;w_span&quot;&gt;&nbsp;&lt;span&nbsp;class=&quot;jg_font_h21_lm&quot;&gt;作者：&lt;/span&gt;${creator}&nbsp;&lt;/span&gt;&nbsp;&lt;span&nbsp;class=&quot;w_span&quot;&gt;&nbsp;&lt;span&nbsp;class=&quot;jg_font_h21_lm&quot;&gt;出版日期:&lt;/span&gt;&lt;span&nbsp;class=&quot;jg_font_h21_nr&quot;&gt;${publishDate}&lt;/span&gt;&nbsp;&lt;/span&gt;&nbsp;&lt;span&nbsp;class=&quot;w_span&quot;&gt;&nbsp;&lt;span&nbsp;class=&quot;jg_font_h21_lm&quot;&gt;介质格式:&lt;/span&gt;&lt;span&nbsp;class=&quot;jg_font_h21_nr&quot;&gt;${FormatType}&lt;/span&gt;&nbsp;&lt;/span&gt;&nbsp;&lt;span&nbsp;class=&quot;w_span&quot;&gt;&nbsp;&lt;span&nbsp;class=&quot;jg_font_h21_lm&quot;&gt;时长信息:&lt;/span&gt;&lt;span&nbsp;class=&quot;jg_font_h21_nr&quot;&gt;${Duration}&lt;/span&gt;&nbsp;&lt;/span&gt;&nbsp;&lt;span&nbsp;class=&quot;w_span&quot;&gt;&nbsp;&lt;span&nbsp;class=&quot;jg_font_h21_lm&quot;&gt;浏览次数:&lt;/span&gt;&lt;span&nbsp;class=&quot;jg_font_h21_nr&quot;&gt;${HitCount}&lt;/span&gt;&nbsp;&lt;/span&gt;&nbsp;&lt;p&gt;&nbsp;&lt;span&nbsp;class=&quot;w_span&quot;&gt;&nbsp;&lt;span&nbsp;class=&quot;jg_font_h21_zy&quot;&nbsp;style=&quot;line-height:20px;margin-top:5px;float:left;&quot;&nbsp;title=&quot;${Introduction}&quot;&gt;&nbsp;${ShortIntroduction}&nbsp;&lt;/span&gt;&nbsp;&lt;/span&gt;&nbsp;&lt;/p&gt;&nbsp;&lt;/td&gt;&nbsp;&lt;/tr&gt;&nbsp;&lt;/table&gt;&nbsp;&lt;/td&gt;&nbsp;&lt;/tr&gt;&nbsp;&lt;/table&gt;&nbsp;&lt;/div&gt;&nbsp;&lt;/td&gt;&nbsp;&lt;/tr&gt;",
             "_ZVING_PAGEINDEX": idx, "_ZVING_PAGETOTAL": 10}
        ),
        "_ZVING_URL": "/medical/medbooks/browse/articleList.zhtml"
    }

book_link=[]
task_ls=[]
pool=ThreadPoolExecutor(max_workers=16)
articleId_pattern = r'articleId=(\d+)'
book_pattern = r'bookId=(\d+)'

def request(each):
    while True:
        try:
            response = requests.post(url, headers=headers, data=get_data(each))
            if response.status_code!=200:
                print("非法的响应码",response.status_code)
                continue
            ls = re.findall(book_pattern, response.text)
            book_link.extend(ls)
            ls = list(set(ls))
            book_link.extend(ls)
            print("len(book_link)",len(book_link),"ls[0]", ls[0],each,"done","len(ls)",len(ls))
            break
        except:
            print(traceback.format_exc())
            time.sleep(1)
            continue

# bookId_pattern = r'bookId=(\d+)'
# pattern = r'<a\shref="(.*?)".*?>'

for each in tqdm.tqdm(range(1)):
    task_ls.append(pool.submit(request,each))
    if len(task_ls) % 16 ==0 :
        concurrent.futures.wait(task_ls)
        task_ls.clear()
concurrent.futures.wait(task_ls)
book_link=list(set(book_link))
print(len(book_link))
with open("讲座-图书分类.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(book_link))