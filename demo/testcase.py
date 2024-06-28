from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def test_login(self):
        user = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        pwd = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        login = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )

        user.send_keys("standard_user")
        pwd.send_keys("secret_sauce")
        login.click()


    def test_add_product_to_cart(self):
        self.test_login() 
        add = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "add-to-cart-sauce-labs-backpack"))
        )
        add.click()
        cart = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart.click()
        checkout = self.driver.find_element(By.NAME, "checkout")
        checkout.click()

if __name__ == "__main__":
    unittest.main()
