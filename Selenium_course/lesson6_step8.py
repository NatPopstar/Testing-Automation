from selenium import webdriver
import time
link = "http://suninjuly.github.io/registration1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_class_name("first")
	input1.send_keys("Marina")
	input2 = browser.find_element_by_class_name("second")
	input2.send_keys("Ivanova")
	input3 = browser.find_element_by_class_name("third")
	input3.send_keys("marina@mail.com")
	button = browser.find_element_by_xpath("//button[text()='Submit']")
	button.click()
	time.sleep(1)
	welcome_text_elt = browser.find_element_by_tag_name("h1")
	welcome_text = welcome_text_elt.tex
	 assert "Congratulations! You have successfully registered!" == welcome_text
finally:
	time.sleep(10)
	browser.quit()

