# 패키지 install
import requests
from bs4 import BeautifulSoup
import openpyxl
import datetime

# Workbook 생성
wb = openpyxl.Workbook()

# Sheet 활성
sheet = wb.active

# 데이터프레임 내 변수명 생성
sheet.append(["순위", "챔피언", "승률"])
# 데이터 크롤링 과정
raw = requests.get('https://www.op.gg/champion/statistics')
html = BeautifulSoup(raw.text, 'html.parser') 

container = html.select('tbody.tabltem.champion-trend-tier-TOP')

for con in container:
    r = con.select_one('td.rank') # 순위
    c = con.select_one('td.champion') #챔피언이름
    v = con.select_one('td.value') # 승률

    # sheet 내 각 행에 데이터 추가
    sheet.append([r,c,v])

# 엑셀 제목을 날짜별로 저장
dt = datetime.datetime.now()
filename = 'opgg_' + dt.strftime("%Y_%m_%d")
f = open(filename + '.xlsx', 'w')
wb.save(filename + '.xlsx')
 # 종료
f.close()