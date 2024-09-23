#!/usr/bin/env python
# coding: utf-8

# In[27]:


import selenium.webdriver
#from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

Name=[]
Location=[]
Salary=[]

driver=selenium.webdriver.Chrome()
chrome_options=Options()
#driver=webdriver.chrome(service=Service(ChromeDriverManager().install(),options=chrome_options))
driver.maximize_window()
driver.get("http://www.naukri.com")

#To 

input=driver.find_element('xpath','/html/body/div[1]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input')
input.send_keys("Data Scientist")

search=driver.find_element('xpath',"/html/body/div[1]/div[7]/div/div/div[6]").click()
location_filter=driver.find_element('xpath','/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/i').click()
salary_filter=driver.find_element('xpath','/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/i').click()

for i in range(1,10):
    try:
        name_element=driver.find('xpath','/html/body/div/div/main/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/a')
        Name.append(name_element.text)
    except:
        Name.append("")
        
    try:
        location_element=driver.find('xpath','/html/body/div/div/main/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div/span[3]/span/span')
        Location.append(name_element.text)
    except:
        Location.append("") 
        
    try:
        salary_element=driver.find('xpath','/html/body/div/div/main/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div/span[2]/span/span')
        Salary.append(name_element.text)
    except:
        Salary.append("") 
        
        
Data_records={'Job_Name':Name,"Location":Location,"Salary":Salary}
        df=pd.DataFrame(Data_records)
    
        


# In[ ]:





# In[ ]:





# In[ ]:




