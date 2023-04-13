from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:/Program Files/chromedriver.exe')
driver = webdriver.Chrome(service=s)
##########################CONSENT################################


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
# add any desired Chrome options here

driver = webdriver.Chrome(service=s,options=chrome_options)

driver.get('https://uk.finance.yahoo.com/crypto/')

driver.implicitly_wait(5)

consent_button = driver.find_element(by=By.CLASS_NAME, value="btn.secondary.reject-all")


consent_button.click()

time.sleep(5)

driver.implicitly_wait(5)

###############################SCRAPE TABLE 1#############################################


# find the table element
table = driver.find_element(By.CSS_SELECTOR, '#scr-res-table')

# find all the rows in the table
rows = table.find_elements(By.TAG_NAME, 'tr')

# create an empty list to store the data
crypdata = []

# loop through the rows and extract the data for each row
for row in rows:
        # find the columns in the row
    cols = row.find_elements(By.TAG_NAME, 'td')
        # check if there are columns (i.e., not a header row)
    if len(cols) > 0:
          # create a dictionary to store the data for this row
        row_data = {
            'Currency': cols[0].text,
            'Symbol': cols[1].text,
            'Last Price': cols[2].text,
            'Change': cols[3].text,
            '% Change': cols[4].text,
            'Market Time': cols[5].text,
            'Volume': cols[6].text
        }
        # append the row data to the list of data
        crypdata.append(row_data)


print(crypdata)

time.sleep(5)
###############################SCRAPE TABLE 2#############################################
nextbutton = driver.find_element(by=By.XPATH, value='//*[@id="scr-res-table"]/div[2]/button[3]')
nextbutton.click()

time.sleep(8)

crypdata1 = []
table1 = driver.find_element(By.CSS_SELECTOR, '#scr-res-table')


rows1 = table1.find_elements(By.TAG_NAME, 'tr')
for row in rows1:
        # find the columns in the row
    cols1 = row.find_elements(By.TAG_NAME, 'td')
        # check if there are columns (i.e., not a header row)
    if len(cols1) > 0:
          # create a dictionary to store the data for this row
        row_data1 = {
            'Currency': cols1[0].text,
            'Symbol': cols1[1].text,
            'Last Price': cols1[2].text,
            'Change': cols1[3].text,
            '% Change': cols1[4].text,
            'Market Time': cols1[5].text,
            'Volume': cols1[6].text
        }
        # append the row data to the list of data
        crypdata1.append(row_data1)

print(crypdata1)

time.sleep(5)

###############################SCRAPE TABLE 2#############################################
nextbutton = driver.find_element(by=By.XPATH, value='//*[@id="scr-res-table"]/div[2]/button[3]')
nextbutton.click()

time.sleep(8)

crypdata2 = []
table2 = driver.find_element(By.CSS_SELECTOR, '#scr-res-table')


rows2 = table2.find_elements(By.TAG_NAME, 'tr')
for row in rows2:
        # find the columns in the row
    cols2 = row.find_elements(By.TAG_NAME, 'td')
        # check if there are columns (i.e., not a header row)
    if len(cols2) > 0:
          # create a dictionary to store the data for this row
        row_data2 = {
            'Currency': cols2[0].text,
            'Symbol': cols2[1].text,
            'Last Price': cols2[2].text,
            'Change': cols2[3].text,
            '% Change': cols2[4].text,
            'Market Time': cols2[5].text,
            'Volume': cols2[6].text
        }
        # append the row data to the list of data
        crypdata2.append(row_data2)

print(crypdata2)

time.sleep(5)



# print the data
#print(crypdata)

# close the webdriver
driver.quit()


