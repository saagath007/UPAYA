from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
import random

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qa-carry.upaya.com.np/users/login")

    def test_login(self):
        #login
        user = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        pwd = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        login = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Log in']"))
        )

        user.send_keys("roshan")
        pwd.send_keys("zxcv123")
        login.click()
        time.sleep(2)

        #Going to create trips
        self.driver.find_element(By.LINK_TEXT,"Create Trips").click()
        time.sleep(1)

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(text(), 'Requirements and Preferences')]"))).click()
        
        #customer field
        javascript = 'document.querySelectorAll("button")[2].click()'
        self.driver.execute_script(javascript)

        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[role=\"listbox\"]")))

        javascript = 'return document.querySelectorAll("[role=\'option\']").length'
        h_count = self.driver.execute_script(javascript)
        print(f'Customer Name: {h_count}')

        # h = random.randint(0, h_count - 1)
        h = 0

        javascript = 'return document.querySelectorAll("[role=\'option\']")[{}].innerText'.format(h)
        entered_value = self.driver.execute_script(javascript)

        javascript = 'document.querySelectorAll("[role=\'option\']")[{}].click()'.format(h)
        self.driver.execute_script(javascript)
        print(f'Customer Name: {entered_value}')
        time.sleep(2)

        end_date = self.driver.find_element(By.ID, "info.endDate")
        end_date.click()
        end_date.send_keys("07")
        end_date.send_keys("05")
        end_date.send_keys("2024")
        time.sleep(3)

        #Pickup Location
        javascript = 'document.querySelectorAll("button")[5].click()'
        self.driver.execute_script(javascript)

        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[role=\"listbox\"]")))

        javascript = 'return document.querySelectorAll("[role=\'option\']").length'
        h_count = self.driver.execute_script(javascript)
        print(f'Pickup Location: {h_count}')
        
        h = 0

        javascript = 'return document.querySelectorAll("[role=\'option\']")[{}].innerText'.format(h)
        entered_value = self.driver.execute_script(javascript)

        javascript = 'document.querySelectorAll("[role=\'option\']")[{}].click()'.format(h)
        self.driver.execute_script(javascript)
        print(f'Pickup Location: {entered_value}')
        time.sleep(2)

        #Pickup Location details
        Ldetails = self.driver.find_element(By.NAME, "location.pickupRemarks")
        Ldetails.click()
        Ldetails.send_keys("New Baneshwor")

        #DropOff Location
        javascript = 'document.querySelectorAll("button")[6].click()'
        self.driver.execute_script(javascript)

        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[role=\"listbox\"]")))

        javascript = 'return document.querySelectorAll("[role=\'option\']").length'
        h_count = self.driver.execute_script(javascript)
        print(f'DropOff Location: {h_count}')
        
        h = 2

        javascript = 'return document.querySelectorAll("[role=\'option\']")[{}].innerText'.format(h)
        entered_value = self.driver.execute_script(javascript)

        javascript = 'document.querySelectorAll("[role=\'option\']")[{}].click()'.format(h)
        self.driver.execute_script(javascript)
        print(f'Dropoff Location: {entered_value}')
        time.sleep(2)

        #DropOff Location details
        Ddetails = self.driver.find_element(By.NAME, "location.dropOffRemarks")
        Ddetails.click()
        Ddetails.send_keys("Lakeside Pokhara")

        #Types of goods
        javascript = 'document.querySelectorAll("button")[7].click()'
        self.driver.execute_script(javascript)

        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[role=\"listbox\"]")))

        javascript = 'return document.querySelectorAll("[role=\'option\']").length'
        h_count = self.driver.execute_script(javascript)
        print(f'Types of Goods: {h_count}')
        
        h = 4

        javascript = 'return document.querySelectorAll("[role=\'option\']")[{}].innerText'.format(h)
        entered_value = self.driver.execute_script(javascript)

        javascript = 'document.querySelectorAll("[role=\'option\']")[{}].click()'.format(h)
        self.driver.execute_script(javascript)
        print(f'Types of Goods: {entered_value}')
        time.sleep(2)

        #Vehicle type and Number of vehicles
        javascript = 'document.querySelectorAll("button")[9].click()'
        self.driver.execute_script(javascript)

        WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[role=\"listbox\"]")))

        javascript = 'return document.querySelectorAll("[role=\'option\']").length'
        h_count = self.driver.execute_script(javascript)
        print(f'Vehicle Type: {h_count}')
        
        h = 0

        javascript = 'return document.querySelectorAll("[role=\'option\']")[{}].innerText'.format(h)
        entered_value = self.driver.execute_script(javascript)

        javascript = 'document.querySelectorAll("[role=\'option\']")[{}].click()'.format(h)
        self.driver.execute_script(javascript)
        print(f'Vehicle Type: {entered_value}')
        time.sleep(2)

        NumberofV = self.driver.find_element(By.NAME, "requirements.vehicle.noOfVehicles")
        NumberofV.click()
        NumberofV.send_keys("1")

        #Contacted channel
        Contacted = self.driver.find_element(By.NAME, "contacts.contacts.0.channel")
        Contacted.click()
        Contacted.send_keys("985100000")

        #Estimated fair
        Estimated_fair = self.driver.find_element(By.ID, "offeredFare")
        Estimated_fair.click()
        Estimated_fair.send_keys("20000")

        #Save and Next
        next = self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']")
        next.click()
        time.sleep(3)


# class ODTtrips(unittest.TestCase):

#     def setUp(self):

#         self.driver = webdriver.Chrome()
        
#         self.driver.implicitly_wait(5)


#     def user_login(self, username, password):
#         driver = self.driver

#         driver.get("https://qa-carry.upaya.com.np/")
#         driver.maximize_window()
        
#         username_element = driver.find_element(By.ID, "username")
#         password_element = driver.find_element(By.ID, "password")

#         username_element.send_keys(username)
#         password_element.send_keys(password)

#         driver.find_element(By.CSS_SELECTOR,"button").click()       #login successfully

# class CreateTrip():
#         def _init_(self, driver):
#              self.driver = driver

#         def create_trip(self): 
#             driver = self.driver
#             driver.find_element(By.LINK_TEXT,"Create Trips").click()
#             time.sleep(1)

#             WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
#                     (By.XPATH, "//*[contains(text(), 'Requirements and Preferences')]"))).click()
            
#             #customer field
#             javascript = 'document.querySelectorAll("button")[2].click()'
#             self.driver.execute_script(javascript)

#             WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(
#                     (By.CSS_SELECTOR, "[role=\"listbox\"]")))

#             javascript = 'return document.querySelectorAll("[role=\'option\']").length'
#             h_count = driver.execute_script(javascript)
#             print(f'Customer Name: {h_count}')

#             # h = random.randint(0, h_count - 1)
#             h = 0

#             javascript = 'return document.querySelectorAll("[role=\'option\']")[{}].innerText'.format(h)
#             entered_value = self.driver.execute_script(javascript)

#             javascript = 'document.querySelectorAll("[role=\'option\']")[{}].click()'.format(h)
#             self.driver.execute_script(javascript)
#             print(f'Customer Name: {entered_value}')
#             time.sleep(2)









#         def test_login(self):

#                 self.user_login(username="roshan", password="zxcv123")      #login 
                
#                 # # self.request_trip()          #request trip



        # def tearDown(self):
        #     time.sleep(20)
        #     self.driver.quit()



       

if __name__ == "__main__":
    unittest.main()


# class Test(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.maximize_window()
#         self.driver.get("https://qa-carry.upaya.com.np/users/login")

#     def test_login(self):
#         user = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located((By.NAME, "username"))
#         )
#         pwd = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located((By.NAME, "password"))
#         )
#         login = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Log in']"))
#         )

#         user.send_keys("roshan")
#         pwd.send_keys("zxcv123")
#         login.click()
#         time.sleep(2)

#     def test_Createtrip(self):
#         self.test_login() 
        
#         create = WebDriverWait(self.driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Create Trips']"))
#         )
#         create.click()
#         time.sleep(3)
#         WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
#             (By.XPATH, "//*[contains(text(), 'Requirements and preferences']"))).click()
#         time.sleep(3)
        
#         # element = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search customers"]')
#         # element.click()
        
#         customer = 'document.querySelectorAll("button")[2].click()'
#         self.driver.execute_script(customer)

#         WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located(
#             (By.CSS_SELECTOR, "[role=\"listbox\"]")))

#         customer = 'return document.querySelectorAll("[role=\'option\']").length'
#         h_count = self.driver.execute_script(customer)
#         print(f'Customer name: {h_count}')


#         # h = random.randint(0, h_count - 1)
#         h = 0

#         customer = 'return document.querySelectorAll("[role=\'option\']")[{}].innerText'.format(h)
#         entered_value = self.driver.execute_script(customer)

#         customer = 'document.querySelectorAll("[role=\'option\']")[{}].click()'.format(h)
#         self.driver.execute_script(customer)
#         print(f'Customer Name: {entered_value}')
#         time.sleep(2)

#         # NHPL = WebDriverWait(self.driver, 10).until(
#         #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Nepal Hydro Pvt Ltd( ✓)')]"))
#         # )
#         # NHPL.click()
#         # time.sleep(2)



   
#         # pickupL = self.driver.find_element(By.XPATH, "//input[@id='headlessui-combobox-input-:ru:']")
#         # pickupL.click()
#         # pickupL.send_keys("Kathmandu")


#         # Ldetails = self.driver.find_element(By.ID, "location.pickupRemarks")
#         # Ldetails.click()
#         # Ldetails.send_keys("New Baneshwor")
#         # # time.sleep(2)

#         # dropoffL = self.driver.find_element(By.ID, "headlessui-combobox-input-:rp:")
#         # dropoffL.click()
#         # dropoffL.send_keys("Chitwan")
#         # CHT = self.driver.find_element(By.XPATH, "//span[@class='block truncate font-normal']")
#         # CHT.click()
#         # time.sleep(2)


 