import time
from const_file import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
username.send_keys("Admin")
passwrod.send_keys("admin123")
loginbutton.click()
pim = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
pim.click()
search_emp_code = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input")
search_emp_code.send_keys("0001")
time.sleep(5)
click_search = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
click_search.click()
a =  driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")
result = a.text
print(result)
print(type(result))
found = "(1) Record Found"
print(type(found))
notfound = "No Records Found"
if result == found:
    delete = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]/i")
    delete.click()
    time.sleep(5)
    msg = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div[2]/p")
    print(msg.text)
    delete_emp = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div/div/div[3]/button[2]")
    delete_emp.click()

else:
    print("No UserID Found")