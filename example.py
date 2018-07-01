from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

try:
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=options)

    driver.get("https://www.google.com")

    driver.close()
except Exception, e:
    print str(e)
    driver.close()
