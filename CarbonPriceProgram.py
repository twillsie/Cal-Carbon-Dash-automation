#Import libraries
import urllib2
from bs4 import BeautifulSoup

#create output document
f = open('CarbonPrice.txt','w')

#create soup
soup = BeautifulSoup(urllib2.urlopen('https://www.theice.com/marketdata/DelayedMarkets.shtml?productId=3418&hubId=4080').read())
table = soup.find('table', {"class":"data default borderless"})

#find content & write to output document. if it doesn't exist, write 0
#The "last" field will either be the 2nd or 3rd column. This code tests
#which one it is in order to pull the correct field
try:
        first_th = table.find('th')
        second_th = first_th.findNext('th')
        if second_th.contents[0] == 'Last':
                td_tag = table.find('td', text = 'Dec13')
                next_td_tag = td_tag.findNext('td')
                f.write (next_td_tag.contents[0])
        else:
                third_th = second_th.findNext('th')
                if third_th.contents[0] == 'Last':
                        td_tag = table.find('td', text = 'Dec13')
                        next_td_tag = td_tag.findNext('td')
                        third_td_tag = next_td_tag.findNext('td')
                        f.write (third_td_tag.contents[0])   
                else:
                        f.write ('Error')
except AttributeError:
	f.write('Error')

f.close()
