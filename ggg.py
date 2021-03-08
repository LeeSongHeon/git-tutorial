# 패키지 install
import requests
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from openpyxl import Workbook
import datetime


# Workbook 생성
wb = Workbook()
# sheet 활성
ws = wb.create_sheet('opgg')
# 데이터프레임 내 변수명 생성
ws.append(['순위', '변동순위', '챔피언이름', '승률', '픽률'])
# 데이터 크롤링 과정
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        for tr_tag in bs.select('tr')[1:]:
            td_tags = tr_tag.select('td')
            title = [
                  td_tags[0].get_text(), #순위
                  td_tags[1].get_text(), #변동순위
                  td_tags[3].get_text(), # 챔피언이름
                  td_tags[4].get_text(), # 승률
                  td_tags[5].get_text(), # 픽률 
            ]
    except AttributeError as e:
        return None
    return title

title = getTitle("https://www.op.gg/champion/statistics")
if title == None:
    print('Title could not be found')
else:
    print(title)




    # sheet 내 각 행에 데이터 추가
    ws.append(title)

# 엑셀 제목을 날짜별로 저장
dt = datetime.datetime.now()
filename = 'opgg_' + dt.strftime("%Y_%m_%d")
wb.save(filename + '.xlsx')