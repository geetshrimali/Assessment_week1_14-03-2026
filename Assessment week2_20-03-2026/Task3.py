from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 15)

search = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search.send_keys("Selenium Python")

suggested = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li")))

for i in suggested:
    print(i.text)

suggested[0].click()
driver.quit()