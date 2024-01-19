import os
from itertools import zip_longest
import requests
TOKEN = 'YOUR BOT TOKEN'
chat_id = "6004481260"
directory = 'D:/TT/CrystalDiskInfo9_2_1/Smart'
path = os.listdir(directory)
files = os.listdir(directory + '/' + path[0])
needsword = ['05', 'PowerOnHours', 'Temperature', 'C5']
f = open('D:/TT/start_sklad.bat', 'r')
lines = f.readlines()[1:2]
for line in lines:
    ttname = line[147:-6]
if 'SA400' in path[0]:
    needsword.clear()
    needsword.append('AA'), needsword.append('Temperature'), needsword.append(
        'PowerOnHours'), needsword.append('C4')
print(needsword)
if 'SSD 870' in path[0]:
    needsword.clear()
    needsword.append('05='), needsword.append(
        'B3'), needsword.append('Temperature'), needsword.append('PowerOnHours')
if 'SSD 980' in path[0]:
    needsword.clear()
    needsword.append('03='), needsword.append(
        'Temperature'), needsword.append('PowerOnHours'), needsword.append('Date')
if 'WDC' in path[0]:
    needsword.clear()
    needsword.append('05='), needsword.append(
        'Temperature'), needsword.append('PowerOnHours'), needsword.append('Date')
f = open(
    "D:/TT/CrystalDiskInfo9_2_1/Smart" + "/" + path[0] + "/" + "Smart.ini", 'r')
lines = f.readlines()
textfile = open('D:/TT/CrystalDiskInfo9_2_1/log.txt', 'w')
for line in lines:
    if needsword[0] in line or needsword[1] in line or needsword[2] in line or needsword[3] in line:
        if '05' in line or 'C4' in line:
            textfile.write('Переназначенных сектора: ' + line)
        elif 'C5' in line or 'B3' in line:
            textfile.write('Кандидатов на переназначение: ' + line)
        else:
            textfile.write(line)
textfile.close()
f = open('D:/TT/CrystalDiskInfo9_2_1/log.txt', 'r')
lines = f.readlines()
for line in lines:
    if 'Temperature' in line:
        t = int(line[13:-2])
t = t + 100
if t > 70:
    message = "Alarm " + ttname
    url = f"https://api.telegram.org/bot{
        TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()
try:
    with open('D:/TT/CrystalDiskInfo9_2_1/log.txt') as first_file, open('D:/TT/CrystalDiskInfo9_2_1/logout.txt') as second_file:
        for first_line, second_line in zip_longest(first_file, second_file):
            if 'PowerOnHours' in first_line or 'Date' in first_line or 'Temperature' in first_line:
                continue
            if first_line != second_line:
                message = "Alarm " + ttname
                url = f"https://api.telegram.org/bot{
                    TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
                requests.get(url).json()
                break
except:
    True
