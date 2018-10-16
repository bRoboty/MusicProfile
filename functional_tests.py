#!/usr/bin/env python3

"""
"""

import os, sys

from selenium import webdriver
from time import sleep


doDebug = True

try:
	id = sys.argv[1]
except IndexError as err:
	print("usage: %s <your ID>" % (sys.argv[0], ),
		  file=sys.stderr)
	sys.exit(1)


browser = webdriver.Firefox()

browser.get(
	'https://music.163.com/user/home?id=%s' %(id, ))
sleep(5)

user_iframe = browser.find_element_by_id('g_iframe')
browser.switch_to.frame(user_iframe)

username = browser.title
if doDebug: 
	# print("username.text: ", username.text)
	print("username: ", username)


alllinks = browser.find_elements_by_tag_name('a')
usefullinks = []
for link in alllinks:
	if doDebug: print("link.text by tag a: ", link.text)
	if "动态" in link.text:
		usefullinks.append(link.get_attribute('href'))
	elif "关注" in link.text:
		usefullinks.append(link.get_attribute('href'))
	elif "粉丝" in link.text:
		usefullinks.append(link.get_attribute('href'))

if doDebug: print(usefullinks)
