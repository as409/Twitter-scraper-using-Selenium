import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

url = "https://twitter.com/search?q="
username = "akku_jack"
password = "Oms@iram"
browser = webdriver.Chrome()
query = 'modi'
url = url +query


browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(5):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.2)

tweets= browser.find_elements_by_class_name('tweet-text')

for tweet in tweets:
	print(tweet.text)