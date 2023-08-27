from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_driver_path = Service("D:\Chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://ovago.com/")
driver.maximize_window()

sign_up_but = driver.find_element(By.CSS_SELECTOR, "#menu > div > div.menu__body > div.menu__section.menu__personal > "
                                                   "a.header__item.menu__item.auth-modal")
sign_up_but.click()


# reg_but = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#auth-login > div.authentication__title-block >"
#                                                " div.authentication__subtitle > a"))
# )
#
# reg_but.click()

email_form = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "AccountForm[email]"))
      )
email_form.send_keys("42toks@gmail.com")
email_form.send_keys(Keys.ENTER)


pass_form = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "AccountForm[password]"))
      )
pass_form.send_keys("1234Qweqw")
pass_form.send_keys(Keys.ENTER)


continue_but = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".authentication__fieldset button"))
      )

continue_but.click()


user_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#header-user-dropdown > "
                                                 "div.user.header__dropdown-toggler.dropdown-toggler > div > div > img"))
)

user_dropdown.click()

sign_out_but = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "user-menu__logout"))
)
sign_out_but.click()

time.sleep(5)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.maximize_window()
# num_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # num_articles.click()
# view_source = driver.find_element(By.LINK_TEXT, "View source")
# # view_source.click()
# # search_button = driver.find_element(By.CSS_SELECTOR, "#searchform > button")
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# # search_button.click()
# search.send_keys(Keys.ENTER)
# time.sleep(5)

driver.quit()
