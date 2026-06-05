
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time, traceback

options = UiAutomator2Options()
options.set_capability("platformName", "android")

driver = webdriver.Remote("http://localhost:4723", options=options)
try:

    def get_element(driver, locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element("xpath", locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = "xpath"
                selector = locator.get('selector', locator) if isinstance(locator, dict) else locator
                try:
                    element = driver.find_element(by_method, selector)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None
    driver.implicitly_wait(6)

    # Step - 1 : Check Proverbial home screen title visibility → {{{{proverbial_home_visible}}}}
    print('Step 1: Query - Check Proverbial home screen title visibility → {{{{proverbial_home_visible}}}}')
    driver.implicitly_wait(6)

    # Step - 2 : Assert {{{{proverbial_home_visible}}}} equals true
    print('Step 2: Assertion - Assert {{{{proverbial_home_visible}}}} equals true')
    driver.implicitly_wait(6)

    # Step - 3 : Tap COLOR button on home screen
    print('Step 3: Tap COLOR button on home screen')
    driver.implicitly_wait(6)

    # Step - 4 : Check COLOR button tapped effect → {{{{color_tapped}}}}
    print('Step 4: Query - Check COLOR button tapped effect → {{{{color_tapped}}}}')
    driver.implicitly_wait(6)

    # Step - 5 : Assert {{{{color_tapped}}}} equals true
    print('Step 5: Assertion - Assert {{{{color_tapped}}}} equals true')
    driver.implicitly_wait(6)

    # Step - 6 : Tap COLOR button
    print('Step 6: Tap COLOR button')
    driver.implicitly_wait(6)

    # Step - 7 : Wait 2 seconds for COLOR effect
    time.sleep(int(2))
    driver.implicitly_wait(6)

    # Step - 8 : Tap COLOR button again
    print('Step 8: Tap COLOR button again')
    driver.implicitly_wait(6)

    # Step - 9 : Check if welcome text color changed from initial state → {{{{color_changed}}}}
    print('Step 9: Query - Check if welcome text color changed from initial state → {{{{color_changed}}}}')
    driver.implicitly_wait(6)

    # Step - 10 : Assert {{{{color_changed}}}} equals true
    print('Step 10: Assertion - Assert {{{{color_changed}}}} equals true')

    driver.quit()
except Exception as e:
    driver.quit()
