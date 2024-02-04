import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



chrome_driver_options = webdriver.ChromeOptions()
chrome_driver_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_driver_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID, "cookie")
store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div")

items = [item.get_attribute("id") for item in store_items[:-1]]

dur = time.time() + 5
laps = time.time() + 5 * 60

while True:
    cookie.click()
   
    if time.time() > dur:
        store_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        prices = [int(price.text.split(" - ")[1].replace(",", ""))  for price in store_prices[:-1]]
        money = int(driver.find_element(By.ID, "money").text)
        affordable_price = [0 for i in range(len(items))]
        for index, price in enumerate(prices,):
            if money > price:
                affordable_price[index] = price
                max_index = affordable_price.index(max(affordable_price))
        expensive = items[max_index]
        # print(expensive)
        driver.find_element(By.ID, f"{expensive}").click()

        dur = time.time() + 5

    if time.time() > laps:
        cps = driver.find_element(By.ID, "cps")
        print(cps.text)
        break

        






driver.quit()
