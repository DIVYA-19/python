import time
import urllib.request
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

try:
    os.mkdir('downloads')
except FileExistsError:
    pass

#path to web driver chrome or firefox any browser. You can download that from selenium official site
browser = webdriver.Chrome("C:\\Users\\ACER\\Downloads\\chromedriver_win32\\chromedriver.exe")
browser.get("https://www.google.com/")
url = browser.current_url
#print(url)
name = browser.find_element_by_name('q')
name.send_keys('sushant singn rajput',Keys.ENTER)
elem = browser.find_element_by_link_text('Images')
elem.get_attribute('href')
elem.click()
value = 0
for i in range(20):
    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #for scrolling down to load more images
    browser.execute_script("scrollBy("+ str(value) +",+1000);")
    value += 1000
    time.sleep(3)

elem1 = browser.find_element_by_id('rg_s')
sub = elem1.find_elements_by_tag_name("img")
count = 0
for i in sub:
    src = i.get_attribute('src')
    try:
        if src != None:
            src  = str(src)
            print(src)
            count+=1
            urllib.request.urlretrieve(src, os.path.join('downloads','image'+str(count)+'.jpg'))
        else:
            raise TypeError
    except TypeError:
        print('fail')
