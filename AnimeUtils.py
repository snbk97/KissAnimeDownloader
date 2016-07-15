# __Author__ = snbk97
# heuheuheuhuehuehueeuhehuehuehuehue
from bs4 import BeautifulSoup
from unidecode import unidecode
import base64
import time




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
    driver.delete_all_cookies()
    driver.get(url)
    time.sleep(6)
    data = unidecode(driver.page_source)

    soup = BeautifulSoup(data, "html.parser")
    inter = (soup.find_all('table', attrs={'class': 'listing'})[0])
    finals = inter.find_all('a')
    final_counter = 0
    for final in finals:
        fo = open('anime_links.csv', 'a+')
        
        final_counter += 1
        ep_url = "http://kissanime.to" + final['href']
        ep_name = str(unidecode(final.text)).strip().split('Episode')[1]
        time.sleep(1)
        ep_detail = ep_name + "~" + FetchURL(driver, ep_url)

        fo.write(ep_detail)
        fo.write("\n")
        print ("Link count: " + str(final_counter))
        fo.close()

