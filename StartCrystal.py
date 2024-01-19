import os
import psutil
import shutil
import time
directory = 'D:/TT/CrystalDiskInfo9_2_1/Smart'

try:
    path = os.listdir(directory)
except:
    os.startfile('D:/TT/CrystalDiskInfo9_2_1/DiskInfo64.exe')
while 'Smart' not in 'D:/TT/CrystalDiskInfo9_2_1':
    update_files = os.listdir('D:/TT/CrystalDiskInfo9_2_1')
    if 'Smart' in update_files:
        break
time.sleep(0.5)
for process in (process for process in psutil.process_iter() if process.name() == "DiskInfo64.exe"):
    process.kill()
directory = 'D:/TT/CrystalDiskInfo9_2_1/Smart'
path = os.listdir(directory)
files = os.listdir(directory + '/' + path[0])


def startfile():
    os.startfile('D:/TT/CrystalDiskInfo9_2_1/DiskInfo64.exe')
    while 'Smart.ini' not in 'D:/TT/CrystalDiskInfo9_2_1/Smart/' + path[0]:
        update_files = os.listdir(
            'D:/TT/CrystalDiskInfo9_2_1/Smart/' + path[0])
        if 'Smart.ini' in update_files:
            break
    time.sleep(0.2)
    for process in (process for process in psutil.process_iter() if process.name() == "DiskInfo64.exe"):
        process.kill()


try:
    shutil.copyfile('D:/TT/CrystalDiskInfo9_2_1/log.txt',
                    'D:/TT/CrystalDiskInfo9_2_1/logout.txt')
except:
    True


try:
    os.remove('D:/TT/CrystalDiskInfo9_2_1/Smart/' + path[0] + '/' 'Smart.ini')
except:
    startfile()
update_files = os.listdir('D:/TT/CrystalDiskInfo9_2_1/Smart/' + path[0])
if 'Smart.ini' not in update_files:
    startfile()
os.system(
    'runas /user:tt /savecred "D:/TT/CrystalDiskInfo9_2_1/CreateLog.exe"')
