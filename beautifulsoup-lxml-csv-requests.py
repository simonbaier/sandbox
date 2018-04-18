from bs4 import BeautifulSoup
import requests
# import csv
import lxml

# import sys
# %pwd


## from sendex youtube: https://www.youtube.com/watch?v=aIPqt-OdmS0
## import bs4 as bs
## import urllib.request
## source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
## Beautiful Soup 4 documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/


# xpath = '//*[@id="templateHeader"]/table[2]/tbody/tr/td/table/tbody/tr/td/div[3]/ul'
# selector = '#templateHeader > table.mcnTextBlock > tbody > tr > td > table > tbody > tr > td > div:nth-child(7) > ul'


# open('url.txt')  #


url = 'https://us13.campaign-archive.com/feed?u=cf75f40d0e0438abbbcb0345d&id=92280c9f09'
source = requests.get(url).text


soup = BeautifulSoup(source,'lxml')
soup.prettify()
# soup.find()

import csv
csv_file = open('output.csv', 'w')  # python ?
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['date','event','link'])   # write header row



for x in soup.find_all('li'):
    date = '4/18/2018'
    link = x.a['href']
#    print(link)
    event = x.a.text
#    print(event)
    csv_writer.writerow(['date', 'event', 'link'])
