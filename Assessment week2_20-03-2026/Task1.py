from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.amazon.in/')

wait = WebDriverWait(driver, 30)

driver.maximize_window()
sleep(1)
title = driver.title
if title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in":
    print("title verified")

url = driver.current_url
if url == "https://www.amazon.in/":
    print("current url verified")

dropbox = wait.until(EC.presence_of_element_located((By.XPATH,"//select[@id = 'searchDropdownBox']")))
dropbox.click()

select = Select(dropbox)

select.select_by_visible_text('Books')

search = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id = 'twotabsearchtextbox']")))
search.send_keys("Harry Potter", Keys.ENTER)

name = wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@role = 'listitem']/descendant::h2[1]/span")))
for i in range(0, 5):
    print(name[i].text)

prod = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@role = 'listitem']/descendant::h2[1]/ancestor::a[1]")))
prod.click()
sleep(3)
driver.quit()

