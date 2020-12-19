from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://mbasic.facebook.com")
html = driver.page_source
print(html)
