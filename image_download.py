import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#as selenium is open source and very easy to use
#images can be downloaded in many ways
#I choose Google, because  it is easy to download
def download_image(keyword):
	#inorder to execute test scripts on Google chrome browser, ChromeDriver should be used
	browser = webdriver.Chrome("chromedriver.exe")
	#loads the provided url in the Google Chrome
	browser.get("https://www.google.com/")
	#getting element that has name 'q' - search bar
	name = browser.find_element_by_name('q')
	#sending keys to the search bar and performing enter
	#then results will appear in the window
	name.send_keys(keyword,Keys.ENTER)
	#getting link element that has text name as 'Images'
	elem = browser.find_element_by_link_text('Images')
	#getting url of the 'Images'
	elem.get_attribute('href')
	#clicking the images link
	elem.click()
	#Each image is wrapped in a div element
	#all div elements of images are also wrapped in div element(parent element)
	#getting parent div element of images
	elem1 = browser.find_element_by_id('rg_s')
	#finding img tag in parent div element
	sub = elem1.find_elements_by_tag_name("img")
	count = 0
	#some image links may be None so avoid errors, try...except have been used
	for i in sub:
	    src = i.get_attribute('src')
	    if count == 0:
	        try:
	            if src != None:
	                src  = str(src)
	                count+=1
	                image_name = src.split('/')
	                urllib.request.urlretrieve(src, image_name[-1].split('.')[0] +'.jpg')
	            else:
	                raise TypeError
	        except TypeError:
	            print('fail')
	    else:
	        break

	browser.close()
	browser.quit()

if __name__ == '__main__':
	keyword = input("Enter keyord:")
	download_image(keyword)
