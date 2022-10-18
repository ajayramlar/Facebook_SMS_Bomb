from selenium import webdriver
import time
browser = webdriver.Chrome('chromedriver.exe')
for x in range(20):
	browser.get('https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0')
	number = browser.find_element_by_xpath('//*[@id="identify_email"]')
	did_submit = browser.find_element_by_name('did_submit')
	number.send_keys('premsai.kapireddy@gmail.com')  //even entering phone number is ok
	did_submit.click()
	time.sleep(20)   //delay can be changed by your internet speed
	submit = browser.find_element_by_xpath('//*[@id="initiate_interstitial"]/div[3]/div/div[1]/button')
	submit.click()
	time.sleep(20)  //enter how many times u want to do