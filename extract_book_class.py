import json

import requests
import tqdm

headers = {
    "Accept": "text/plain, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "JSESSIONID=62D9ABFE6F4BE1B0F9BDC01EEA8DC794; UniqueID=tXVvDg8wtzcRYHDU1714987500016; Sites=_0; route=6956ef56584808585a187954e8100680; __root_domain_v=.ipmph.com; _qddaz=QD.117814985994423; Hm_lvt_ec31b23a3a54fb0e85df69fc93bd5de9=1715133669; Hm_lpvt_ec31b23a3a54fb0e85df69fc93bd5de9=1715133669; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218f4d38f5b7190d-084705f8463bb28-4c657b58-1327104-18f4d38f5b8ab6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%A4%BE%E4%BA%A4%E7%BD%91%E7%AB%99%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fopen.weixin.qq.com%2F%22%7D%2C%22identities%22%3A%22%5Cn%2F1vqr%7B%5Cu0003v%5Cu0003%5Cbln%7B%7C%7B%5Cbz%7C%5Cu0004%5Cu0002lvq%2FG%2F%3EEsAq%40EsBoD%3EF%3Dq%3A%3DEAD%3DBsEAC%40oo%3FE%3AApCBDoBE%3A%3E%40%3FD%3E%3DA%3A%3EEsAq%40EsBoEnoC%2F9%2F1vqr%7B%5Cu0003v%5Cu0003%5Cblp%7C%7Cxvrlvq%2FG%2F%3EEsBC%3Dn%3FrDFnpD%3A%3D%40%3D%3FEop%40FFDBnA%3AApCBDoBE%3A%3E%40%3FD%3E%3DA%3A%3EEsBC%3Dn%3FrDnF%3DE%2F%5Cf%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218f4d38f5b58b4-0001e573ac901e574-4c657b58-1327104-18f4d38f5b61a1e%22%7D; _qddab=3-ml9d5r.lvxlm4ia; undefined_vq=103",
    "Origin": "https://medbooks.ipmph.com",
    "Pragma": "no-cache",
    "Referer": "https://medbooks.ipmph.com/medical/medbooks/browse/resourceTree_lazyLoad.zhtml?resourceType=ReferenceBook&classType=6&classCode=",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "Chromium;v=124, Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
}
url = "https://medbooks.ipmph.com/medical/resourceTree/lazyload"
ls=[{'id': '38152', 'name': '一般理论(90)'},
 {'id': '38166', 'name': '现状与发展(10)'},
 {'id': '38167', 'name': '实验医学,医学实验(43)'},
 {'id': '38170', 'name': '预防医学,卫生学(670)'},
 {'id': '38522', 'name': '中国医学(64)'},
 {'id': '38893', 'name': '基础医学(309)'},
 {'id': '39691', 'name': '临床医学(960)'},
 {'id': '39955', 'name': '内科学(1051)'},
 {'id': '40634', 'name': '外科学(768)'},
 {'id': '41097', 'name': '妇产科学(191)'},
 {'id': '41273', 'name': '儿科学(215)'},
 {'id': '41325', 'name': '肿瘤学(376)'},
 {'id': '41564', 'name': '神经病学与精神病学(318)'},
 {'id': '41693', 'name': '皮肤病学与性病学(63)'},
 {'id': '41833', 'name': '耳鼻咽喉科学(67)'},
 {'id': '41991', 'name': '眼科学(153)'},
 {'id': '42105', 'name': '口腔科学(141)'},
 {'id': '42200', 'name': '特种医学(149)'},
 {'id': '42722', 'name': '药学(131)'}]

total=[]
def request(x):
    data = {
        "id": x["id"],
        "n": x["name"],
        "lv": "1",
        "resourceType": "ReferenceBook",
        "classType": "6",
        "Code": ""
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code==200:
        data=response.json()
        for each in data:
            if each.get("open",None)=="true":
                total.append(each)
            else:
                ls.append(each)

while ls!=[]:
    item=ls.pop()
    request(item)
    print(len(ls))

with open(f"./total.json","w",encoding="utf-8") as f:
    f.write(json.dumps(total))