from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = Service("D:\Chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

element = driver.find_element(By.CLASS_NAME, "a-offscreen")

print(element.text)

driver.close()

driver.quit()

