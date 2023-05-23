from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  

driver.get("https://www.utest.com/signup/personal")

wait = WebDriverWait(driver, 10)
nombre_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))


nombre_input.send_keys("Pepito")
apellido_input = driver.find_element(By.NAME, "lastName")
apellido_input.send_keys("Perez")

email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("pepitoperez@gmail.com")

mes_nacimiento_select = Select(driver.find_element(By.NAME, "birthMonth"))
mes_nacimiento_select.select_by_visible_text("January")  

dia_nacimiento_select = Select(driver.find_element(By.NAME, "birthDay"))
dia_nacimiento_select.select_by_visible_text("16") 

año_nacimiento_select = Select(driver.find_element(By.NAME, "birthYear"))
año_nacimiento_select.select_by_visible_text("1996")  


idioma_select = Select(driver.find_element(By.NAME, "languages"))
idioma_select.select_by_visible_text("English")  

siguiente_button = driver.find_element(By.XPATH, "//a[contains(text(),'Next - Location')]")

siguiente_button.click()


wait = WebDriverWait(driver, 10)

ciudad_input = driver.find_element(By.NAME, "city")
ciudad_input.send_keys("Nezahualcoyotl")


codigo_postal_input = driver.find_element(By.NAME, "postalCode")
codigo_postal_input.send_keys("57500")

pais_select = Select(driver.find_element(By.NAME, "countryId"))
pais_select.select_by_visible_text("México")


siguiente_button = driver.find_element(By.XPATH, "//a[contains(text(),'Next - Devices')]")

siguiente_button.click()


wait = WebDriverWait(driver, 10)

fabricante_select = driver.find_element(By.NAME, "handsetMakerId")
fabricante_select.send_keys("Xiaomi")

device_input = driver.find_element(By.XPATH, "//input[@name='handsetModelId']")
device_input.send_keys("Redmi Note 12 Pro")

so_select = driver.find_element(By.NAME, "handsetPlatformId")
so_select.send_keys("Android 12")

siguiente_button = driver.find_element(By.XPATH, "//a[contains(text(),'Next - Last Step')]")
siguiente_button.click()


wait = WebDriverWait(driver, 10)

password_input = driver.find_element(By.XPATH, "//input[@name='password']")
password_input.send_keys("Qwe098.2023")

confirm_password_input = driver.find_element(By.XPATH, "//input[@name='confirmPassword']")
confirm_password_input.send_keys("Qwe098.2023")

terms_checkbox = driver.find_element(By.XPATH, "//input[@name='terms']")
terms_checkbox.click()

privacy_checkbox = driver.find_element(By.XPATH, "//input[@name='privacy']")
privacy_checkbox.click()

complete_button = driver.find_element(By.XPATH, "//button[contains(text(),'Complete Setup')]")
complete_button.click()

driver.quit()