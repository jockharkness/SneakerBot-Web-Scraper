from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


def UrlGenWithSize():
    URL_base = "https://www.sneakerboy.com/shop-sneakers/"
    URL_shoe = "gucci-mens-tennis-1977-ss20gucc121.html"
    return (URL_base + URL_shoe)

def CheckStock(myUrl):
    try:
        driver = webdriver.Chrome()
        driver.get(myUrl)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ember-select"))) #  "btn product-form__add-to-cart is-added")))
        username = driver.find_element_by_class_name("ember-select")
        options = username.find_elements_by_tag_name("option")
        optionsList = []
        for option in options:
            optionsList.append(option.get_attribute("innerHTML"))
        optionsList.remove(optionsList[0])
        for sizes in optionsList:
            if not ("SOLD OUT" in sizes):
                print("Size " + sizes + " is available")

    finally:
        driver.quit()


def addToCart(myUrl):
    driver = webdriver.Chrome()
    driver.get(myUrl)
    kicks = "EU39.5 (UK5.5 US6)"
    select = Select(driver.find_element_by_class_name("ember-select"))
    select.select_by_visible_text('EU39.5 (UK5.5 US6)')
    #element = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.CLASS_NAME, "ember-select")))
    driver.find_element_by_xpath("//BUTTON[@class='btn btn-secondary btn-buy add-cart'][text()='BUY']").click()
    #checkout_button = driver.find_element_by_class_name("button-checkout") #btn-secondary pull-right")
    driver.implicitly_wait(10)
    #ActionChains(driver).move_to_element(checkout_button).click(checkout_button).perform()
    #WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//A[@href='#'][text()='Checkout']")))
    driver.find_element_by_xpath("//A[@href='#'][text()='Checkout']").click()

    email = driver.find_element_by_id("checkoutemail")
    email.send_keys("moitchmootson@gmail.com")
    password = driver.find_element_by_id("checkoutpassword")
    password.send_keys("Moitch01!")
    driver.find_element_by_xpath("(//A[@href='#'][text()='Login'][text()='Login'])[2]").click()
    #gotocheckout = driver.find_element_by_link_text("Goto Checkout")
    #gotocheckout.click()
    driver.find_element_by_xpath("(//A[@href='https://www.sneakerboy.com/cart.php?site=sneakerboy&a=checkout'][text()='Goto Checkout'][text()='Goto Checkout'])[2]").click()


url = UrlGenWithSize()
#CheckStock(url)
addToCart(url)



