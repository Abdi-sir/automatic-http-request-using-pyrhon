# selenium 3
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.get("http://localhost:3000/login")
n="admin@gmail.com"


i = 0
while i < 100:
   driver.find_element("id","email").send_keys(n)
   driver.find_element("id","pass").send_keys(i)
   driver.find_element("id","Login").submit()
   i+=1


