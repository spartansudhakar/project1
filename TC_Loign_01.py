from const_file import *
username.send_keys("Admin")
passwrod.send_keys("admin123")
loginbutton.click()
af_login_url = driver.current_url
if bf_login_url != af_login_url:
    print("You Are Logged in Sucessfully")
else:
    print("Username or Password may be Incorrect")