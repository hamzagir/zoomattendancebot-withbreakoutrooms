#tt manage
import datetime
import time

import os
from time import monotonic, strftime
x = datetime.datetime.now()
p=x.strftime("%a")
if p=="Mon":
   current_time=x.strftime("%X")
   thishour=x.strftime("%H")
   thismin=x.strftime("%M")
   thissec=x.strftime("%S")
   remhours=9-int(thishour)
   remmin=55-int(thismin)
   remtime=(remhours*60*60)+(remmin*60)+int(thissec)
   time.sleep(remtime)
   os.system('python zoomfullbot.py')
   time.sleep(3600)
   os.system('python zoomfullbot.py')
   time.sleep(3600)
   os.system('python zoomfullbot.py')
   time.sleep(3600)
   os.system('python zoomfullbot.py')
   
elif p=="Tue":
    current_time=x.strftime("%X")
    thishour=x.strftime("%H")
    thismin=x.strftime("%M")
    thissec=x.strftime("%S")
    remhours=9-int(thishour)
    remmin=55-int(thismin)
    remtime=(remhours*60*60)+(remmin*60)+int(thissec)
    time.sleep(remtime)
    os.system('python zoomfullbot.py')
    time.sleep(7200)
    os.system('python zoomfullbot.py')
    time.sleep(3600)
    os.system('python zoomfullbot.py')
elif p=="Wed":
    current_time=x.strftime("%X")
    thishour=x.strftime("%H")
    thismin=x.strftime("%M")
    thissec=x.strftime("%S")
    remhours=10-int(thishour)
    remmin=55-int(thismin)
    remtime=(remhours*60*60)+(remmin*60)+int(thissec)
    time.sleep(remtime)
    os.system('python zoomfullbot.py')
    time.sleep(3600)
    os.system('python zoomfullbot.py')
    time.sleep(3600)
    os.system('python zoomfullbot.py')
elif p=="Thu":
    current_time=x.strftime("%X")
    thishour=x.strftime("%H")
    thismin=x.strftime("%M")
    thissec=x.strftime("%S")
    remhours=9-int(thishour)
    remmin=55-int(thismin)
    remtime=(remhours*60*60)+(remmin*60)+int(thissec)
    time.sleep(remtime)
    os.system('python zoomfullbot.py')
    time.sleep(3600)
    os.system('python zoomfullbot.py')
    time.sleep(3600)
    os.system('python zoomfullbot.py')
    time.sleep(3600)
    os.system('python zoomfullbot.py')
elif p=="Fri":
    current_time=x.strftime("%X")
    thishour=x.strftime("%H")
    thismin=x.strftime("%M")
    thissec=x.strftime("%S")
    remhours=10-int(thishour)
    remmin=55-int(thismin)
    remtime=(remhours*60*60)+(remmin*60)+int(thissec)
    time.sleep(remtime)
    os.system('python zoomfullbot.py')
    time.sleep(7200)
    os.system('python zoomfullbot.py')
else:
    print("Its a Holiday Bitch")




   
   

   


