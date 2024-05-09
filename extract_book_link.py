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
url = "https://medbooks.ipmph.com/medical/medbooks/browse/bookList.zhtml"

with open("./total.json","r",encoding="utf-8") as f:
    data=json.loads(f.read())

# https://medbooks.ipmph.com/medical/medbooks/browse/detailBook.zhtml?bookId=39972146&resourceType=ReferenceBook
def request(x):
    params = {
        "resourceType": "ReferenceBook",
        "classType": "6",
        "classCode": x["code"]
    }
    response = requests.get(url, headers=headers, params=params)
    with open(f"./html/{x['code']}.html","w",encoding="utf-8") as f:
        f.write(response.text)

for each in tqdm.tqdm(data):
    request(each)