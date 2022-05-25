import requests
from bs4 import BeautifulSoup
import datetime
import csv

response = requests.get(
    "https://www.cwb.gov.tw/V8/C/W/Observe/MOD/24hr/46692.html?T=297")
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find_all("tr")

# print(soup.prettify())

path = str(datetime.date.today()) + '_LOG.csv'
print(path)

with open(path,'w+', newline="") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['time', 'humidity', 'pressure'])
    for r in result:
        hum = float(r.find("td",headers="hum").text)
        pre = float(r.find("td",headers="pre").text)
        ti = r.find("th", headers = "time").text
        # print(result.prettify())
        writer.writerow([ti, hum, pre])
