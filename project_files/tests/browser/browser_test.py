from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://localhost:5050")

driver.quit()
