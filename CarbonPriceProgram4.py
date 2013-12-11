#Import libraries
import urllib2
from bs4 import BeautifulSoup
import datetime
import smtplib

#create output document
f = open('CarbonPrice.txt','a')

#start a new line
f.write('\n')

#create soup
soup = BeautifulSoup(urllib2.urlopen('https://www.theice.com/marketdata/DelayedMarkets.shtml?productId=3418&hubId=4080').read())
table = soup.find('table', {"class":"data default borderless"})

#Find and record "last" price
price_idx = -1
for idx, th in enumerate(table.find_all('th')):
    # Find the column index of price
    if th.get_text() == 'Last':
        price_idx = idx
        break

for tr in table.find_all('tr'):
    # Extract the content of each column in a list
    td_contents = [td.get_text() for td in tr.find_all('td')]
    # If this row matches our requirement, take the Last column
    if 'Dec13' in td_contents:
        pricevar = td_contents[price_idx]

f.write(pricevar)
f.write(',')

#Find and record time
time_idx = -1
for idx, th in enumerate(table.find_all('th')):
    # Find the column index of Time
    if th.get_text() == 'Time':
        time_idx = idx
        break

timevar = []
for tr in table.find_all('tr'):
    # Extract the content of each column in a list
    td_contents = [td.get_text() for td in tr.find_all('td')]
    # If this row matches our requirement, take the Time column
    if 'Dec13' in td_contents:
        time_str = td_contents[time_idx]
        # This will capture Thu Dec 05 16:26:24 EST 2013 GMT, convert to datetime object
        time_obj = datetime.datetime.strptime(time_str,'%a %b %d %H:%M:%S EST %Y GMT')
        timevar.append(datetime.datetime.strftime(time_obj,'%x'))

f.write(timevar[0])

#pull timestamp
pulltime = datetime.datetime.now()

#send email with success or failure
fromaddr = 'calcarbondash@gmail.com'
toaddrs = 'tucker.willsie@cpisf.org'
msg = "\r\n".join([
    "From: Calcarbondash@gmail.com",
    "To: Tucker.willsie@cpisf.org",
    "Subject: Status of upload",
    "",
    "Upload successful - todays upload was " +str(pricevar)+", "+str(timevar[0])+ ". The time of the pull was "+str(pulltime)
    ])

#credentials
username = 'CalCarbonDash'
password = '465California'

# Send the message via Michelin SMTP server, but don't include the envelope header.
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

f.close()