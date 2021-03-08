# 패키지 install
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import datetime

def zxcsd():
    
    for tr_tag in soup.select('tr')[1:]:
        td_tags = tr_tag.select('td')
        row = [
            td_tags[0].get_text(), #순위
            td_tags[1].get_text(), #변동순위
            td_tags[3].get_text(), # 챔피언이름
            td_tags[4].get_text(), # 승률
            td_tags[5].get_text(), # 픽률 
        ]
    # sheet 내 각 행에 데이터 추가
        ws.append(row)
    return   

