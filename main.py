from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


def click_cookie():
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()


def check_money():
    money = driver.find_element(By.ID, value="money").text
    try:
        money = int(money)
    except ValueError:
        money = money.replace(",", "")
        money = int(money)

    return money


def purchase_upgrade():
    upgrades = []
    store = driver.find_element(By.ID, value="store")
    upgrades_list = store.find_elements(By.TAG_NAME, value="b")
    for upgrade in upgrades_list:
        try:
            cost = upgrade.text.split("-")[1]
            cost = cost.replace(" ", "")
            if "," in cost:
                cost = cost.replace(",","")
            title = upgrade.text.split("-")[0]
            title = title.replace(" ", "")
        except IndexError:
            pass
        else:
            new_upgrade = {
                "Title": title,
                "Cost": int(cost)
            }
            upgrades.append(new_upgrade)
    for upgrade in reversed(upgrades):
        money = check_money()
        if money > upgrade["Cost"]:
            upgrade_to_purchase = driver.find_element(By.ID, value=f"buy{upgrade['Title']}")
            upgrade_to_purchase.click()
            time.sleep(.05)


# stop after 5 minutes
stop = time.time() + 60*5 # 5 minutes
purchase_time = time.time() + 10 # 5 seconds
increase_purchase = time.time() + 60*3
while time.time() < stop:
    if time.time() > purchase_time:
        purchase_upgrade()
        if time.time() < increase_purchase:
            purchase_time = time.time() + 10
        else:
            purchase_time = time.time() + 15
    click_cookie()

# Print cookies/second
cookies_per_second = driver.find_element(By.ID, value="cps")
print(cookies_per_second.text)

driver.quit()
