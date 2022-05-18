import serial
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

serial_port = 'COM3'
baud_rate = 9600
path = "LOG.csv"
ser = serial.Serial(serial_port, baud_rate)

with open(path, 'a', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    while True:
        line = ser.readline().decode("utf-8").strip()

        response = requests.get("https://www.cwb.gov.tw/V8/C/W/Observe/MOD/24hr/46692.html?T=297")
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find("tr")
        hum = result.find("td",headers="hum").text #humidity
        pre = result.find("td",headers="pre").text #pressure
        ti = result.find("th", headers = "time").text #time
        
        print(line, hum, pre, ti)
        writer.writerow([datetime.now(), line, hum, pre, ti])
        f.flush()