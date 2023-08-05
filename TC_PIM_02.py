import time

from const_file import *
username.send_keys("Admin")
passwrod.send_keys("admin123")
loginbutton.click()
pim = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
pim.click()
search_emp_code = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input")
search_emp_code.send_keys("0001")
click_search = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
click_search.click()
time.sleep(5)
a =  driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")
result = a.text
print(result)
print(type(result))
found = "(1) Record Found"
print(type(found))
notfound = "No Records Found"
if result == found:
    edit = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]/i")
    edit.click()
    time.sleep(5)
    driveinglic = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input")
    driveinglic.send_keys("IND-01-07")
    sv = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button").click()
    sv1 = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button").click()
else:
    print("The User ID is Not Found")

