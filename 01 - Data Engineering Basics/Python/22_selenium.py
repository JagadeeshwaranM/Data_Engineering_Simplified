from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(100)
driver.get("http://demo.guru99.com/test/newtours/")
driver.find_element_by_xpath("//tbody/tr[2]/td[2]/input[1]").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").submit()
driver.close()
