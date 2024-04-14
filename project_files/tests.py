from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver


# Create your tests here.
class selenium_browser_test(LiveServerTestCase):
    def test_login(self):
        selenium = webdriver.Chrome()
        selenium.get('http://localhost:8000')
        insert_name = selenium.driver.findElement(By.id('nome'))
