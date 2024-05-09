import json
import os
import traceback
from concurrent.futures.thread import ThreadPoolExecutor

import tqdm

from settings import *
import re
import requests


class medbook:

    def __init__(self):
        self.zhuanzhu_url=""
        self.file_path="./book/专著-图书分类.json"

        with open(self.file_path,"r",encoding="utf-8") as f:
            self.json_data=json.loads(f.read())

        self.pool=ThreadPoolExecutor(max_workers=16)

    def request_book(self,bookid)->list:
        # 请求获取书籍的目录结构数据
        url = "https://medbooks.ipmph.com/medical/medbooks/browse/directory_Tree.zhtml"
        params = {
            "bookId": bookid,
            # "bookId": "16832331",
            "resourceType": "ReferenceBook"
        }
        response = requests.get(url, headers=headers, params=params)
        json_data = re.findall(extract_zNodes, response.text)
        return json_data

    def get_params(self,bookid,code):
        return {
            "directoryId": bookid,
            "articleId": code,
            "resourceType": "ReferenceBook",
            "linkaddress": code
            #     code
        }
    def get_html(self,bookid,code):
        url = "https://medbooks.ipmph.com/medical/medbooks/browse/detailContent_iframe1.zhtml"
        try:
            response = requests.get(url, headers=headers, params=self.get_params(bookid,code))
            if response.status_code !=200:
                return False,response.text
            return True,response.text
        except:
            print(traceback.format_exc())
            return False,None
    def main(self):
        for bookid in tqdm.tqdm(self.json_data,desc=self.file_path):
            directory_tree_nodes=self.request_book(bookid)
            if not os.path.exists(f"./data/{bookid}"):
                os.mkdir(f"./data/{bookid}")
            for every in tqdm.tqdm(directory_tree_nodes,desc=bookid):
                the_id, name, code, belongname, open_if=every
                result,resp=self.get_html(bookid,code)
                if not result:
                    continue
                with open(f"./data/{bookid}/{name}.html", "w", encoding="utf-8") as f:
                    f.write(resp)

if __name__ == '__main__':
    medbook_crawler=medbook()
    medbook_crawler.main()