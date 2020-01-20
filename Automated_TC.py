#Simple test to check if the search returns results.

from selenium import webdriver
import datetime

driver = webdriver.Chrome('/Users/karan.mehra/PycharmProjects/Testing/chromedriver/chromedriver')
driver.get("http://qalab.pl.tivixlabs.com/")

current = datetime.datetime.today().strftime("%m-%d-%Y")
next_date = datetime.datetime.today() + datetime.timedelta(days=1)
next_date = next_date.strftime("%m-%d-%Y")

driver.find_element_by_xpath("//input[@id='model']").send_keys("Suzuki Swift")
driver.find_element_by_xpath("//input[@id='pickup']").send_keys(current)
driver.find_element_by_xpath("//input[@id='dropoff']").send_keys(next_date)
driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()

webelement = driver.find_element_by_xpath("//table[@id='search-results']").is_displayed()

if webelement:
    print("Test Passed")
else:
    print("Test Failed")


