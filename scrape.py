import pandas as pd
import time

import requests
from requests_html import HTMLSession
from selenium import webdriver
session = requests.get('https://www.speedtest.net').text
soup = BeautifulSoup(session, 'lxml')

for keyword in df_keywords.Keyword:
    print(keyword)
    r = session.get('https://google.com/search?q='+keyword)


    ads = r.html.find('.ads-ad')

    for ad in ads:
        ad_link = ad.find('.V0MxL', first=True).absolute_links
        ad_link = next(iter(ad_link))
        ad_headline = ad.find('h3.sA5rQ', first=True).text
        ad_copy = ad.find('.ads-creative', first=True).text
        ad_list.append([keyword, ad_link, ad_headline, ad_copy])

df_ads = pd.DataFrame(ad_list, columns = ['keyword', 'ad_link', 'ad_headline', 'ad_copy'])

for index, row in df_ads.iterrows():
    print('Index: ' + str(index) + ', AdLink: ' + row['adlink'])
    browser = webdriver.Firefox()
    browser.get(row['adlink'])
    browser.quit()