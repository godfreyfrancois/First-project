from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/firefox.exe')
browser = webdriver.Firefox(firefox_binary=binary)

#browser = webdriver.Firefox()

browser.get('https://login.pointclickcare.com/home/userLogin.xhtml')
assert 'PointClickCare' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()