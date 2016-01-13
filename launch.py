import subprocess
import time

print 'Loading daemon...'
time.sleep(3)
subprocess.Popen('python ../main.py')
time.sleep(3)
print 'Loading frontend...'
time.sleep(3)
subprocess.Popen('../frontend/WSOP-win32-x64/WSOP.exe')
print 'Done.'
print ''


