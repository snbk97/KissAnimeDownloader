# __Author__ = snbk97
# heuheuheuhuehuehueeuhehuehuehuehue
from bs4 import BeautifulSoup
from csv2html import c2h
from unidecode import unidecode
import base64
import time
import os


def checkFile():
    fname = "anime_links.csv"
    return os.path.isfile(fname)


def FetchURL(driver, url):

    driver.get(url)
    driver.implicitly_wait(1)
    data = unidecode(driver.page_source)
    soup = BeautifulSoup(data, "html.parser")

    try:
        inter = (soup.find_all('div', attrs={'id': 'divQuality'})[0])
    except:
        exception_string = "[!] Error [!]"
        return exception_string

    finals = inter.find_all('option')

    for final in finals:
        p = str(str(final).split('value=')[1][1:].split('<')[0]).split('\">')
        ret_p = base64.b64decode(p[0])
        break

    return ret_p


def FetchInfo(driver, url):
    if(checkFile()):
        os.remove('anime_links.csv')

    driver.delete_all_cookies()
    driver.get(url)
    time.sleep(6)
    data = unidecode(driver.page_source)

    soup = BeautifulSoup(data, "html.parser")
    inter = (soup.find_all('table', attrs={'class': 'listing'})[0])
    finals = inter.find_all('a')
    final_counter = 0
    for final in finals:
        try:
            fo = open('anime_links.csv', 'a+')

            final_counter += 1
            ep_url = "http://kissanime.to" + final['href']
            ep_name = str(unidecode(final.text)).strip().split('Episode')[1]
            time.sleep(1)
            ep_detail = ep_name + "~" + FetchURL(driver, ep_url)

            fo.write(ep_detail)
            fo.write("\n")
            print ("\b\rEP count: " + str(final_counter))
            fo.close()
        except(IndexError):
            print "[!] Error Occured\nConverting CSV and Quitting"
            c2h(url)
            quit()


def csv2html(anime_name, url):
    fo = open('anime_links.csv', 'rb')
    fh = open('anime_links.html', 'wb')

    fh_pre_data = '''
                <html>
                <head>
                <link href='https://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>
                <style>
                body{
                font-family:'Raleway',Arial;
                }
                </style>
                </head>

                <body>
                <center><h1> <a href="https://github.com/snbk97/KissAnimeDownloader">Kiss Anime Downloader</a></h1></center>
                <hr></br>
                '''
    fh.write(fh_pre_data)
    fh.write("<center><h2><a href=" + url + ">" + anime_name + "</a></h2><br>")

    l = len(fo.readlines()) - 1
    fo.seek(0, 0)
    for i in fo.readlines()[l::-1]:
        ep = i.split('~')[::2][0]
        link = i.split('~')[::-1][0]
        final = "EP " + ep + ': ' + '<a href=' + '"' + link + '"' + '>Link</a>'
        fh.write(final)
        fh.write('</br>')

    fh.close()
    fo.close()
