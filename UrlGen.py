from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def UrlGenWithSize():
    URL_base = "https://kith.com/collections/mens-footwear/products/"
    URL_shoe = "aafy5167"
    return (URL_base + URL_shoe)

def CheckStock(myUrl):
    try:
        driver = webdriver.Chrome()
        driver.get(myUrl)
        WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, "product-form"))) #  "btn product-form__add-to-cart is-added")))
        username = driver.find_elements_by_class_name("product-form")
        print("username equals", username)
        options = username.find_elements_by_tag_name("data-value")
        optionsList = []
        for option in options:
            optionsList.append(option.get_attribute("innerHTML"))
        for sizes in optionsList:
            if sizes.isdigit():
                print("Size " + sizes + " for " + " is available")
    finally:
        driver.quit()

url = UrlGenWithSize()
CheckStock(url)


print(UrlGenWithSize())
