from random import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
def close():
    driver.find_element_by_css_selector('[title="Menu"]').click()
    driver.find_element_by_css_selector('.Ut_N0.n-CQr[title="Log out"]').click()
    driver.close()
wishBucket=["thank you very much","I am very thankful to you","thanks","thank you"]
names=list()
happy = ['happy', "hpy", 'hapy', 'hppy','many']
birthday = ['birthday','bd','barthday','brthday','bday',"b'day",'borthday','return','returns']
def checkMessage(_driver):
	global driver
	driver=_driver
	candidate = driver.find_elements_by_css_selector('[aria-label*="unread message"]')
	for mes in candidate:
		no_of_unread_messages = int(mes.text)
		mes.click()
		li_message = driver.find_elements_by_css_selector("[class$='message-in focusable-list-item'] ._3Whw5.selectable-text.invisible-space.copyable-text")[-no_of_unread_messages:]
		names = driver.find_elements_by_css_selector("[class$='message-in focusable-list-item'] [class^='zGvn8 color']")[-no_of_unread_messages:]
		i=0
		for unread_div in li_message:
			li = unread_div.text.lower().split()
			if len(names) == 0:
				if 'hbd' in li:
					send_message(choice(wishBucket))
					#+":" +driver.find_element_by_css_selector('._33QME ._3ko75._5h6Y_._3Whw5').text
				elif len(li) >= 2 and (li[0] in happy) and (li[1] in birthday):
					send_message(choice(wishBucket))
				continue
			else:
				if "hbd" in li:
					returnWish(names[i].text.split())
				elif len(li)>=2 and (li[0] in  happy) and (li[1] in birthday) :
					returnWish(names[i].text.split())
			i += 1
def returnWish(sender):
	if len(sender)==1:
		msg='@'+sender[0]+": "+choice(wishBucket)
		send_message(msg)
	else:
		msg = '@'+sender[-1]+": "+choice(wishBucket)
		send_message(msg)

def send_message(msg):
	if driver.find_element_by_css_selector('[class="_3-cMa _3Whw5"]').text.split(',')[-1]!=' You':
		msg = msg +":"+driver.find_element_by_css_selector('._33QME ._3ko75._5h6Y_._3Whw5').text
	#print(driver.find_element_by_css_selector('[class="_3-cMa _3Whw5"]').text.split(',')[-1])
	inp=driver.find_element_by_css_selector('._3FRCZ.copyable-text.selectable-text[data-tab="1"]')
	inp.send_keys(msg)
	inp.send_keys(Keys.RETURN)

if __name__=="__main__":
	pass


	
