#!/usr/bin/python3
import os,math
command=os.popen('stat -c%s /var/log/syslog')
#bashcommand="state -c%s /var/log/syslog"
#output=subprocess.check_output(['bash','-c', bashcommand])
size=round(int(command.read())/1048576,4)
print(size)
if size>2:
   os.popen('>/var/log/syslog')
   print('file cleared')
else:
   print("Size is lesser than 2MB")
