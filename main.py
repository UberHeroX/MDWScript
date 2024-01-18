from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import datetime
import time
import os
import sys
import threading

def SetupScript():
    print("Skripta aktivirana...")
    import IzakBotScript

def clear_screen():
    # Windows
    if sys.platform == "win32":
        os.system('cls')
   
def CustomTimer():
 while True:
    current_time = datetime.datetime.now()
    time_left = target_time - current_time
    if time_left.total_seconds() > 0:
        clear_screen() 
        time_left_str = str(time_left).split('.')[0]
        print(f"Vreme do aktivacije: {time_left_str}")
        time.sleep(1)  
    else:
        break


scheduler = BlockingScheduler()


#Vreme za aktivaciju. 
#Godina|Mesec|Dan|Sat|Minut|Sekund

Godina= 2024
Mesec= 1
Dan= 18
Sat= 15
Minut= 5
Sekunda= 20

now = datetime.datetime.now()
target_time = now.replace(hour=Sat, minute=Minut, second=Sekunda)

scheduler.add_job(SetupScript, 'date', run_date=datetime.datetime(Godina, Mesec, Dan, Sat, Minut, Sekunda))
print("Tajmer uspesno postavljen")

countdown_thread = threading.Thread(target=CustomTimer)
countdown_thread.start()


scheduler.start()











