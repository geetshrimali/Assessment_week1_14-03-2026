from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

options = webdriver.ChromeOptions()
options.binary_location = brave_path

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 10)

driver.get("https://automationexercise.com/signup")

sleep(1)

driver.find_element(By.NAME, "name").send_keys("abab")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("6060@outlook.com")

driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

# wait for gender radio button
wait.until(EC.visibility_of_element_located((By.ID, "id_gender1"))).click()

newsletter = driver.find_element(By.ID, "newsletter")
offers = driver.find_element(By.ID, "optin")

newsletter.click()
offers.click()

print("Newsletter selected:", newsletter.is_selected())
print("Offers selected:", offers.is_selected())