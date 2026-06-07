
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time,requests,re,os, traceback
try:
    from condition import Condition, ResolvedCondition, ConcatenationOperator
except Exception as e:
    pass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lambdatest_selenium_driver import smartui_snapshot
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options=options)
try:

    actions = ActionChains(driver)
    def get_element(driver,locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element(By.XPATH, locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = By.XPATH if str(locator['isXPath']).lower() == "true" else By.CSS_SELECTOR
                try:
                    element = driver.find_element(by_method, locator['selector'])
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None

    class element_to_be_input_and_text(object):
        def __call__(self, driver):
            focused_element = driver.execute_script("return document.activeElement;")
            if focused_element.tag_name == "input" or focused_element.tag_name == "textarea" or focused_element.get_attribute("contenteditable") == "true":
                return focused_element
            else:
                return False

    def select_option(select_element, option):
        select = Select(select_element)
        select.select_by_value(option)
    driver.implicitly_wait(6)

    # Step - 1 : Open https://ecommerce-playground.lambdatest.io/
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.implicitly_wait(6)

    # Step - 2 : Click on the search input field with placeholder 'Search For Products'
    element_locators = ["//div[@id='entry_217822']//div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/input[1]", '#entry_217822 > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 3 : Click on the search input field in top center with placeholder 'Search For Products'
    element_locators = ["//div[@id='entry_217822']//div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/input[1]", '#entry_217822 > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 4 : Type in search input field with placeholder 'Search For Products' 'iphone'
    element_locators = ["//div[@id='entry_217822']//div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/input[1]", '#entry_217822 > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)
    driver.execute_script("arguments[0].value = '';", element)
    if element.get_attribute("pattern") and '[0-9]{2}' in element.get_attribute("pattern"):
        for char in 'iphone':
            element.send_keys(char)
    else:
        element.send_keys('iphone')
    driver.implicitly_wait(6)

    # Step - 5 : Click on the SEARCH button in the top right corner of the search dropdown
    element_locators = ["//div[@id='entry_217822']//div[1]/form[1]/div[1]/div[2]/button[1]", "//button[text()='Search']", '#entry_217822 > div:nth-child(1) > form:nth-child(1) > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)', "//button[contains(text(),'Search')]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 6 : Hover first product in search results
    element_locators = ["//a[@id='mz-product-grid-image-40-212469']//div[1]/div[1]/img[1]", "//a[@id='mz-product-grid-image-40-212469']//div[1]/div[1]/img[1]", '#mz-product-grid-image-40-212469 > div:nth-child(1) > div:nth-child(1) > img:nth-child(1)', '#mz-product-grid-image-40-212469 > div:nth-child(1) > div:nth-child(1) > img:nth-child(1)']
    element = get_element(driver,element_locators)

    actions.move_to_element(element).perform()
    driver.implicitly_wait(6)

    # Step - 7 : Click on the add to cart icon overlay on the first product image
    element_locators = ["//div[@id='entry_212469']//div[1]/div[1]/div[1]/div[1]/div[2]/button[1]", '#entry_212469 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)']
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 8 : Click View Cart button in cart popup
    element_locators = ["//a[contains(text(),'View Cart')]", '.toast > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)', '.toast > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)', "//div[contains(@class,'toast') and contains(@class,'fade') and contains(@class,'show')]//div[2]/div[2]/div[1]/a[1]", "//div[contains(@class,'toast') and contains(@class,'fade') and contains(@class,'show')]//div[2]/div[2]/div[1]/a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 9 : Get quantity column text → {{quantity_options}}
        html = element.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
        try:
            print("html:", html)
            match = re.search(fr"", html)
        
            result = match.group(1) if match else None
        except Exception as e:
            print("Regex not found in query")
        quantity_options = result
    
    print("quantity_options:", quantity_options)
    driver.implicitly_wait(6)

    # Step - 10 : Read Product name text → {{product_name_text}}
        html = element.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
        try:
            print("html:", html)
            match = re.search(fr"", html)
        
            result = match.group(1) if match else None
        except Exception as e:
            print("Regex not found in query")
        product_name_text = result
    
    print("product_name_text:", product_name_text)
    driver.implicitly_wait(6)

    # Step - 11 : Assert {{product_name_text}} contains 'iPhone'
        html = element.get_attribute('outerHTML').replace('"', "'").replace("\n", "")
        try:
            print("html:", html)
            match = re.search(fr"", html)
        
            result = match.group(1) if match else None
        except Exception as e:
            print("Regex not found in query")
        product_name_text = result
    
    print("product_name_text:", product_name_text)

    driver.quit()
except Exception as e:
    driver.quit()
