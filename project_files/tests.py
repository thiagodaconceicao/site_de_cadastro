from django.test import TestCase
from django.test import LiveServerTestCase

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create your tests here.
class selenium_browser_test(LiveServerTestCase):
    def test_login(self):
        selenium = webdriver.Chrome()
        result = selenium.get('http://localhost:8000')
        selenium.implicitly_wait(3)

        print(result)

        nome_element = selenium.find_element(By.ID, 'nome')
        senha_element = selenium.find_element(By.ID, 'senha')
        button_enviar = selenium.find_element(By.ID, 'enviar')

        nome_element.send_keys('teste')
        senha_element.send_keys('123456')
        button_enviar.click()


         
