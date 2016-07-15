# __Author__ = snbk97
# heuheuheuhuehuehueeuhehuehuehuehue
import AnimeUtils
import os
from selenium import webdriver
import sys

#url = sys.argv[1]
url = "http://kissanime.to/Anime/Barakamon"
if('http://kissanime.to' in url):
    if(os.uname()[0] == 'Linux' or os.uname()[0] == 'Darwin'):
        browser = webdriver.PhantomJS()
        AnimeUtils.FetchInfo(browser, url)
        browser.close()
        os.system('pkill phantomjs')  # Windows(NT) imcompatible
else:
	print "Only supports kissamine.to links"