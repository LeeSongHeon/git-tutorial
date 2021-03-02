import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import datetime

req = requests.get('https://www.op.gg/champion/statistics')
raw = req.text
html = BeautifulSoup(raw, 'html.parser')

champion_name = soup.select('tbody.tabltem.champion-trend-tier-TOP')


name = []
rank = []
value = []
for name in champion_name:
    print('champion_name')
    print('33333333333333333333333')