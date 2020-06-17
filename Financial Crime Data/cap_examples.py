#Need url_list.txt file, chromedriver.exe
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from bs4 import BeautifulSoup
import csv

#To open the text file and retrieve all the urls to scrape from
urls = []
for line in open("url_list4.txt"):
	urls.append(line)
#print(urls)

chromedriver = "C:/Users/Joel Hon/Documents/Joel/NUS/Y3S2/IS4010/Indeed-resume-scraper-master (2)/Indeed-resume-scraper-master/chromedriver.exe"
#baseurl = "https://cite.case.law/f-appx/679/873/"
driver = webdriver.Chrome(executable_path=chromedriver)
cases = []
counter = 1
for url in urls:
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, 'html.parser')
	casebody = soup.find_all('p')
	case_list = [i.getText() for i in casebody]
	case = ' '.join(case_list)
	#print(case)
	cases.append(case)
	# print(cases)
	# print(len(cases))
	# if counter == 3:
	#break
	# counter += 1
with open('case4.txt', 'w', encoding="utf-8") as f:
	for item in cases:
		f.write("%s\n" % item)

driver.close()