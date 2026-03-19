from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()


driver.get("https://www.wikipedia.org/")
sleep(2)


search_box = driver.find_element(By.ID, "searchInput")
print("Search box found")

english_lang = driver.find_element(By.ID, "js-link-box-en")
print("English language found:", english_lang.text)

logo = driver.find_element(By.CSS_SELECTOR, "div.central-textlogo img")
print("Wikipedia logo located")

languages = driver.find_elements(By.CSS_SELECTOR, "div.central-featured-lang a")
print("Number of language links:", len(languages))

english_lang.click()
sleep(2)

driver.back()
sleep(2)

driver.forward()
sleep(2)

driver.refresh()
sleep(2)

print("Final Page Title:", driver.title)

driver.quit()
