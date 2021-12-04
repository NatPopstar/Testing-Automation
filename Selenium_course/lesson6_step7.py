from selenium import webdriver
import time
#from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")

try:
	input1 = browser.find_element_by_tag_name("input")
	input1.send_keys("Ivan")
	input2 = browser.find_element_by_name("last_name")
	input2.send_keys("Petrov")
	input3 = browser.find_element_by_class_name("city")
	input3.send_keys("Smolensk")
	input4 = browser.find_element_by_id("country")
	input4.send_keys("Russia")
	button = browser.find_element_by_xpath("//button[text()='Submit']")
	#button = browser.find_elements(By.xpath,"button.Submit")
	#button = browser.find_elements(By.xpath("html/body/div/form/div/button[text()='Submit']"))
	button.click()
finally:
	time.sleep(15)
	browser.quit()


