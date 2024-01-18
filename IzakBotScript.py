from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import SeliniumInstaller as SelInstal
import ApschedulerInstaller as APSInstal
import time

SelInstal.CheckIfSeliniumIsInstalled()

APSInstal.PackageInstaller()

#uveriti se da je Webdriver na dobrom mestu: https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/win64/chromedriver-win64.zip
webdriver_service = Service("C:/Users/Uros/Downloads/chromedriver-win64/chromedriver.exe") 

login_url = "https://www.mdw.ac.at/raumkalender/"

username = 'ban-izak' #Tvoj Username

password = '314159cl0ck' #Tvoj Password

broj_dana = 15

broj_sobe= 4

ImeKorisnika = "Izak Ban" #Ime korisnika koje zelis

StartHours = 16 #Vreme za poceti

StartMinutes = 15 #uveriti se da je broj deljiv sa 15

EndHours = 19 #vreme za zavrsiti

EndMinutes = 15

#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################

#Nova Sesija

driver = webdriver.Chrome(service=webdriver_service)
driver.get(login_url)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)  #vreme za cekanje

#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#FUNCTIONS

ClickableButton = None
InputButton = None


def GetClickableButton(InputButtons):
  for index, child in enumerate(InputButtons):
     try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(child))
        global ClickableButton
        ClickableButton = child
        break
        
     except TimeoutException:
        print(f"Child element {index} is not clickable within 5 seconds.")

def GetInputableButton(InputButtons):
 for index, child in enumerate(InputButtons):
    if child.is_displayed() and child.is_enabled() and not child.get_attribute('readonly'):
        global InputButton
        InputButton = child
        break
    else:
        print(f"Child element {index} cannot have values inserted.")


def RoomSwitch(case):
    if case == 4:
        return 0
    elif case == 1:
        return 1
    elif case == 2:
        return 2
    else:
        return 3

#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################


# Pronalazi Sajt

button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q-app > div > div.q-page-container.bg-grey-1 > main > div > div > div.column > button")))
button.click()

# Unosi informacije za login

username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys(username)

password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys(password)


#Uloguje se 

buttonLogin = wait.until(EC.presence_of_element_located((By.ID, "kc-login")))
buttonLogin.click()

buttonLogin = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q-app > div > div.q-page-container.bg-grey-1 > main > div > div > div.q-card.q-my-lg.bg-grey-3 > div.column > div:nth-child(1) > div > a")))
buttonLogin.click()

#bira dan

buttonNext = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q-app > div > div.q-page-container.bg-grey-1 > main > div.fc.fc-media-screen.fc-direction-ltr.fc-theme-standard > div.fc-header-toolbar.fc-toolbar.fc-toolbar-ltr > div:nth-child(3) > div > button.fc-next-button.fc-button.fc-button-primary")))
for i in range(broj_dana):
    buttonNext.click()

buttonTerminAnlegen = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q-app > div > div.q-page-container.bg-grey-1 > main > div.fc.fc-media-screen.fc-direction-ltr.fc-theme-standard > div.fc-header-toolbar.fc-toolbar.fc-toolbar-ltr > div:nth-child(3) > button.fc-terminAnlegen-button.fc-button.fc-button-primary")))
buttonTerminAnlegen.click()

#inicijalizuje novi prozor 
NewDateWindow= WebDriverWait (
    driver, 10 ).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]')))

NameBoxEntry = NewDateWindow.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/label')
NameBoxEntry.send_keys(ImeKorisnika)


TimeSlot= NewDateWindow.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div')
TimeSlot.click()

NewTimeWindow= WebDriverWait (
    driver, 10 ).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div[1]/div')))



StartTimeHour= NewTimeWindow.find_element(By.XPATH ,'/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div[1]/div/label[1]')
StartTimeHourChild_elements = StartTimeHour.find_elements(By.CSS_SELECTOR, "*")  
StartTimeHourChild_input_elements = StartTimeHour.find_elements(By.CSS_SELECTOR, "input, textarea")


StartTimeMinute= NewTimeWindow.find_element(By.XPATH ,'/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div[1]/div/label[2]')
StartTimeMinuteChild_elements = StartTimeMinute.find_elements(By.CSS_SELECTOR, "*")  
StartTimeMinute_input_elements = StartTimeMinute.find_elements(By.CSS_SELECTOR, "input, textarea")

EndTimeHour= NewTimeWindow.find_element(By.XPATH ,'/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div/label[1]')
EndTimeHourChild_elements = EndTimeHour.find_elements(By.CSS_SELECTOR, "*")  
EndTimeHourChild_input_elements = EndTimeHour.find_elements(By.CSS_SELECTOR, "input, textarea")



EndTimeMinute= NewTimeWindow.find_element(By.XPATH ,'/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div/label[2]')
EndTimeMinuteChild_elements = EndTimeMinute.find_elements(By.CSS_SELECTOR, "*")  
EndTimeMinuteChild_input_elements = EndTimeMinute.find_elements(By.CSS_SELECTOR, "input, textarea")


GetClickableButton(StartTimeHourChild_elements)
ClickableButton.click()
GetInputableButton(StartTimeHourChild_input_elements)
InputButton.send_keys(StartHours)
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

time.sleep(0.25)

GetClickableButton(StartTimeMinuteChild_elements)
ClickableButton.click()
GetInputableButton(StartTimeMinute_input_elements)
InputButton.send_keys(StartMinutes)
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

time.sleep(0.25)

GetClickableButton(EndTimeHourChild_elements)
ClickableButton.click()
GetInputableButton(EndTimeHourChild_input_elements)
InputButton.send_keys(EndHours)
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()


time.sleep(0.25)

GetClickableButton(EndTimeMinuteChild_elements)
ClickableButton.click()
GetInputableButton(EndTimeMinuteChild_input_elements)
InputButton.send_keys(EndMinutes)
actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

RoomSlot= NewDateWindow.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[4]/div[1]')
RoomSlot.click()

NewRoomMenu= WebDriverWait (
    driver, 10 ).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div[2]/div/div[4]/div[2]/div/label')))
RoomChild_elements = NewRoomMenu.find_elements(By.CSS_SELECTOR, "*")  



GetClickableButton(RoomChild_elements)
ClickableButton.click()
for i in range(RoomSwitch(broj_sobe)+1):
   
 actions.send_keys(Keys.ARROW_DOWN).perform()

actions.send_keys(Keys.ENTER).perform()

FinishButton = NewDateWindow.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div[3]/button[2]')

FinishButton.click()


# Wait for some time (if needed, for the page to load after login)
time.sleep(20)


#Copyright © Uros Panic