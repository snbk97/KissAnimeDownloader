# __Author__ = snbk97
# heuheuheuhuehuehueeuhehuehuehuehue
import KAUtils
from selenium import webdriver
import sys

url = sys.argv[1]

anime = url.split('http://kissanime.to/Anime/')[1]


if('http://kissanime.to' in url):
    browser = webdriver.PhantomJS()
    browser.delete_all_cookies()
    KAUtils.FetchInfo(browser, url)
    browser.close()
    KAUtils.csv2html(anime, url)
    # os.system('pkill phantomjs')  # Windows(NT) imcompatible
else:
    print "Only supports kissamine.to links"
