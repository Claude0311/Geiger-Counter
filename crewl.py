import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

response = requests.get(
    "https://www.cwb.gov.tw/V8/C/W/Observe/MOD/24hr/46692.html?T=297")
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find_all("tr")
print(result[0].prettify())
# print(soup.prettify())
target = str(datetime.now())
for s in [' ','.',':']:
    target = target.replace(s,'')
path = target + '_LOG.csv'
print(path)

with open(path,'w', newline="") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['time', 'humidity', 'pressure', 'temperature'])
    for r in reversed(result):
        hum = (r.find("td",headers="hum").text)
        pre = (r.find("td",headers="pre").text)
        ti = r.find("th", headers = "time").text
        tem = ''
        try:
            tem = r.find("td",headers = "temp").find("span").text
        except:
            tem = ''
        # print(tem)
        # print(result.prettify())
        writer.writerow([ti, hum, pre, tem])
