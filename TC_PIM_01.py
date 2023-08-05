from const_file import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver.implicitly_wait(15)
username.send_keys("Admin")
passwrod.send_keys("admin123")
loginbutton.click()
pim = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
pim.click()
addemp = driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']")
addemp.click()

firstname = driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-firstname']")
middlename = driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-middlename']")
lastname = driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-lastname']")
empid = driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
firstname.send_keys("Orang")
middlename.send_keys("hr")
lastname.send_keys("free suit")
save = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()

nickname = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input")
otherid = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input")
driveingid = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input")
lic_exp_date = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input")
ssn_num = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input")
sin_num = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input")
nationality = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]")
married_or_single = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]")
gender = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span")
militaryservice = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input")
dob = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input")

nickname.send_keys("Shawn")
otherid.send_keys("001122")
driveingid.send_keys("IN 02")
lic_exp_date.send_keys("2023-08-03")
ssn_num.send_keys("00112233")
sin_num.send_keys("012")

nationality.send_keys("i")
nationality.send_keys("i")
nationality.send_keys("i")
married_or_single.send_keys("s")
dob.send_keys("1994-01-01")
gender.click()
militaryservice.send_keys("YES")

smocker = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label")
smocker.click()
save = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button")
save.click()
bloodgp = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]")
bloodgp.send_keys("o")
save2 = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button").click()



