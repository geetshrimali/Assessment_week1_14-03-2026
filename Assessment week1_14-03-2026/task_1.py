from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/login')

driver.maximize_window()

username = driver.find_element(By.CSS_SELECTOR,'input[name = "username"]')
print(username)

password = driver.find_element(By.CSS_SELECTOR,'input[id = "password"]')
print(password)

button = driver.find_element(By.CSS_SELECTOR,'button[type = "submit"]')
print(button)

footer = driver.find_element(By.CSS_SELECTOR,'div[style = "text-align: center;"] a')

print(footer.text)

driver.quit()