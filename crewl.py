import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://www.cwb.gov.tw/V8/C/W/Observe/MOD/24hr/46692.html?T=297")
soup = BeautifulSoup(response.text, "html.parser")
result = soup.find("tr")

hum = result.find("td",headers="hum").text
pre = result.find("td",headers="pre").text
ti = result.find("th", headers = "time").text

print(result.prettify())
print(hum,pre, ti)
