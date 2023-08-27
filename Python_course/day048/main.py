from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("D:\Chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

# driver.get("https://ovago.com/search/WAS-LON/2023-09-10/2023-09-16")


# price_whole = driver.find_element(By.CSS_SELECTOR, "div.search-result-card:nth-child(2) div.search-result-card__price"
#                                                    " > div > form > div > div > div.sr-price-wrap__price-full")
# price_decimal = driver.find_element(By.CLASS_NAME, "sr-price-wrap__price-full")
#
# price_full = "".join(price_whole.text.split("\n")[1:])
#
# print(price_full)


driver.get("https://www.python.org")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_data = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_year = driver.find_elements(By.CSS_SELECTOR, ".event-widget time span")
event_name = driver.find_elements(By.CSS_SELECTOR, "div.medium-widget.event-widget.last > div > ul > li > a")

list_year = [y.get_attribute("innerText") for y in event_year]
list_date = [d.text for d in event_data]
list_name = [n.text for n in event_name]

events = {}
for i in range(len(list_name)):
    events[i] = {
        "time": f"{list_year[i]}{list_date[i]}",
        "name": list_name[i],
    }

print(events)

driver.quit()

