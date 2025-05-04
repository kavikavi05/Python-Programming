from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com/form")

name_field = driver.find_element("name", "username")
name_field.send_keys("Revanth")

submit_button = driver.find_element("name", "submit")
submit_button.click()

print("Form submitted successfully!")
