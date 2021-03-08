# 패키지 install
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import datetime
import zxcsd

# Workbook 생성
wb = Workbook()
# sheet 활성
ws = wb.create_sheet('opgg')
# 데이터프레임 내 변수명 생성
ws.append(['순위', '변동순위', '챔피언이름', '승률', '픽률'])
# 데이터 크롤링 과정
response = requests.get("https://www.op.gg/champion/statistics")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

# 엑셀 제목을 날짜별로 저장
dt = datetime.datetime.now()
filename = 'opgg_' + dt.strftime("%Y_%m_%d")
wb.save(filename + '.xlsx')