import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

class UITesting(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        # options.add_argument('--log-level=2')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service("C:\\Users\\Tirmidzi\\Documents\\Codes\\automation-ui-testing\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.set_window_size(1920, 1080)
        self.driver.get("http://localhost:3000")
    
    def tearDown(self):
        self.driver.close()

    def test_1_register(self):
        # click registration
        elem = self.driver.find_element(By.LINK_TEXT, 'User Registration')
        elem.click()

        # write input
        elem = self.driver.find_element(By.ID, 'lastName')
        elem.clear()
        elem.send_keys("Aflahi")

        elem = self.driver.find_element(By.ID, 'firstName')
        elem.clear()
        elem.send_keys("Tirmidzi")

        elem = self.driver.find_element(By.ID, 'userName')
        elem.clear()
        elem.send_keys("taflahi")

        elem = self.driver.find_element(By.ID, 'email')
        elem.clear()
        elem.send_keys("taflahi@gmail.com")

        # click register
        elem = self.driver.find_element(By.XPATH, '//button[text()="REGISTER"]')
        elem.click()

        time.sleep(5)

        # check registration
        elem = self.driver.find_element(By.XPATH, '//div[text()="taflahi@gmail.com"]')
        self.assertEqual('taflahi@gmail.com', elem.text)

        time.sleep(5)
        
        # delete entry with taflahi@gmail.com
        elem = self.driver.find_element(By.XPATH, '//div[text()="taflahi@gmail.com"]/following-sibling::div')
        elem = elem.find_element(By.TAG_NAME, 'button')
        time.sleep(1)
        elem.click()

        # check is deleted
        time.sleep(10)
        elem = None
        try:
            elem = self.driver.find_element(By.XPATH, '//div[text()="taflahi@gmail.com"]')
        except:
            pass
        self.assertEqual(None, elem)

    def test_2_cards(self):
        # click Card Grid
        elem = self.driver.find_element(By.LINK_TEXT, 'Card Grid')
        elem.click()
        time.sleep(5)
        elem = self.driver.find_elements(By.CLASS_NAME, 'card')

        # check is length = 4
        self.assertEqual(4, len(elem))


if __name__ == '__main__':
    unittest.main()