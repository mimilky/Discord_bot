from bs4 import BeautifulSoup
import requests
import re
import codecs
import wiki

load_url = "https://wiki3.jp/arknightsjp/page/14#content_header_main_content_h2_3"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")


class wiki:
    
     
    def get_url(self, name):
        url = soup.find_all(text=re.compile(name))[0].previous_element["href"]
        if "https://" in url:
            return url
        else:
            return "https://wiki3.jp" + url

        
    
    def get_op_info(self, name):
        load_url = wiki.get_url(name)
        html =  requests.get(load_url)
        
        soup = BeautifulSoup(html.content, "html.parser")

        skill_level = ["7→8","8→9","9→10"]
        elems = []
        all = []

        for i in range(3):
            elems.append(soup.find_all(text=skill_level[i]))
        #elems[スキルレベル][スキルの数(星4だったら2つ)]

        for i in range(len(skill_level)):
            for j in range(len(elems[i])):
                all.append(elems[i][j].next_element.next_element.next_element.text)
        
        for i, _ in enumerate(all):
            all[i] = all[i].encode('cp932', 'ignore')
            all[i] = all[i].decode('cp932')

        return all


wiki = wiki()
