from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

import time
USERNAME = "la tua matricola"
PASSWORD = "la tua password"
ORA_INIZIO = 9
ORA_FINE = 18
GIORNO_INIZIO = 17
GIORNO_FINE = 18

INTERVALLO = 2
ORA1 = ORA_INIZIO
ORA2 = ORA_INIZIO + INTERVALLO
giorni = GIORNO_FINE - GIORNO_INIZIO

driver = webdriver.Chrome('./chromedriver')
driver.get("https://prodigit.uniroma1.it/")
time.sleep(0.1)
#print(driver.title)
#search_bar = driver.find_element_by_name("q")
#search_bar.clear()
#search_bar.send_keys("getting started with python")
#search_bar.send_keys(Keys.RETURN)
accept = driver.find_element_by_xpath('//*[@id="cookieChoiceDismiss"]')
accept.click()
user_id = driver.find_element_by_name("Username")
user_id.send_keys(USERNAME);
user_password = driver.find_element_by_name("Password")
user_password.send_keys(PASSWORD);
enter = driver.find_element_by_xpath('//*[@id="LoginUserFormTable1_b"]/div/table/tbody/tr[2]/td[6]/div/input');
enter.click()
time.sleep(0.5)
link = driver.find_element_by_xpath('/html/body/form/div/table/tbody/tr[3]/td/div/a')
link.click()

timespan = ORA_FINE - ORA_INIZIO

numero_iterazioni = timespan // 2 

if((timespan)%2 != 0):
    numero_iterazioni += 1

for i in range(giorni):
    for j in range(timespan): 
        
        if(len(str(ORA1)) == 1):
            str_ora1 = "0" + str(ORA1)
        else:
            str_ora1 = str(ORA1)
        
        str_ora2 = str(ORA2)
        driver.get("https://prodigit.uniroma1.it/prenotazioni/prenotaaule.nsf/prenotaposto-in-sala-studio-read?openform&salascelta=AULA%20T8%20--%20RM052-E01PTEL052codice=RM052data1=" + str(GIORNO_INIZIO) +"/09/2021ora1=" + str_ora1 + ":00orafine=" + str_ora2 + ":00fine=")

        selectElem = driver.find_element_by_name("alleore1")
        select = Select(selectElem)
        select.select_by_index(0) #se bisogna fare 2 ore, index 0
        time.sleep(0.2)
        check = driver.find_element_by_name("dichiarazione")
        check.click()
        prenota = driver.find_element_by_xpath("/html/body/form/section/article/table[6]/tbody/tr/td[1]/div/a[1]")
        prenota.click()
        ORA1 += 1
   
    GIORNO_INIZIO += 1
    ORA1 = ORA_INIZIO


driver.close()

#prenotaposto-in-sala-studio-read?openform&salascelta=SALA STUDIO Isola G Piano 2%20%-- RM021-L015Gcodice=RM021data1=14/09/2021ora1=08:00orafine=19:00fine=

#https://prodigit.uniroma1.it/prenotazioni/prenotaaule.nsf/prenotaposto-in-sala-studio-read?openform&salascelta=AULA%20T8%20--%20RM052-E01PTEL052codice=RM052data1=13/09/2021ora1=09:00orafine=16:00fine=

#https://prodigit.uniroma1.it/prenotazioni/prenotaaule.nsf/prenotaposto-in-sala-studio-read?openform&salascelta=AULA%20T8%20--%20RM052-E01PTEL052codice=RM052data1=13/09/2021ora1=09:00orafine=16:00fine=

#stringa check green pass
#https://prodigit.uniroma1.it/prenotazioni/prenotaaule.nsf/prenotaposto-in-sala-studio-read?OpenForm&Seq=1&salascelta=AULA%20T8%20--%20RM052-E01PTEL052codice%3DRM052data1%3D13%2F09%2F2021ora1%3D09%3A00orafine%3D16%3A00fine%3D#_RefreshKW_dichiarazione