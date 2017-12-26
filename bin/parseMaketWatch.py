import csv
import urllib
import requests
from bs4 import BeautifulSoup
import re
import datetime
import calendar
import time
import os
import shutil
import sys
import string
import re
from time import gmtime, strftime
from datetime import datetime

###Help sites and notes 
##https://www.crummy.com/software/BeautifulSoup/bs4/doc/

url = "C:/aftab/aftab_personal/python/misc/VIX.html"
##url ="http://www.marketwatch.com/investing/index/vix/options?countrycode=US&showAll=True"
#html = urllib.urlopen(url)
##html = urllib.urlopen(url).read()

soup = BeautifulSoup(open(url), "html.parser")
##soup = BeautifulSoup(response.content, "html.parser")
find1 = soup.findAll('body')
##print(find1)

find_price=find1[0].findAll("p", {'class':re.compile("data bgLast")})[0].text
download_time = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#find3=find2[0].findAll("span", {'class':re.compile("currency")})
#print(find_price)
#sys.exit()

## find table and it contents where class has optiontable eightwide
##find2=find1[0].findAll("table", {'class':re.compile("optiontable eightwide")})
find2=find1[0].findAll("tr", {'class':re.compile("chainrow aright")})

#Logic for reading option price
for find3 in find2:
    find6 =find3.findAll('td')
    
    find601=find6[0].a['title']
    find602=find6[1].text.strip()
    find603=find6[2].text.strip()
    find604=find6[3].text.strip()
    find605=find6[4].text.strip()
    find606=find6[5].text.strip()
    find607=find6[6].text.strip()
    find608=find6[7].text.strip()
    
    find609=find6[8].a['title']
    find610=find6[9].text.strip()
    find611=find6[10].text.strip()
    find612=find6[11].text.strip()
    find613=find6[12].text.strip()
    find614=find6[13].text.strip()
    find615=find6[14].text.strip()


    find615=str.replace(str.replace(find615,' ','0'),',','')
    try:
        float(find615)
    except ValueError:
        find615='0'

    try:
        float(find614)
    except ValueError:
        find614='0'

    try:
        find615=str.replace(str.replace(find615,' ','0'),',','')
        float(find615)
    except ValueError:
        find615='0'

    rowcall =   (find601  + '|' + find602  + '|' + find603  + '|' + find604 + '|' + find605
        + '|' +  find606  + '|' + find607 + '|' + find608 + '|' + download_time + '|' + find_price  )
    
    rowput =  (find609  + '|' + find610 + '|'+  find611  + '|' + find612 +
    '|'+  find613  + '|' +  find614 + '|' +  find615  + '|' + find608 + '|' + download_time + '|' +find_price )  
    
    print(rowcall)
    print(rowput)
       
    ##print(float(str.replace(str.replace(find615,' ','0'),',','')))
    ##sys.exit()

#import re
#https://docs.python.org/2/library/re.html
###  re.sub('VIX','  ',find601)
#text = 'how are u? umberella u! u. U. U@ U# u '
#print re.sub (' [u|U][s,.,?,!,W,#,@ (^a-zA-Z)]', ' you ', text)
#(resutl is following)
#how are you  you berella you  you  you  you  you  yo
 
