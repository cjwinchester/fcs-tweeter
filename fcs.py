from mechanize import Browser
from bs4 import *
import time
import re
from twitter import *

# Step 1: target the table cell with the current status

mech = Browser()

mech.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

mech.set_handle_robots(False)

baseurl = "http://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/ps.html"

page = mech.open(baseurl)
html = page.read()
soup = BeautifulSoup(html)

table = soup.findAll('table')[4]
cells = table.findAll('td')
fcs = cells[19].renderContents()

# Step 2: define email function

def send_email():
            import smtplib
            gmail_user = "XXXXXXXXXXXXX@gmail.com"
            gmail_pwd = "XXXXXXXXXXXXXXXXX"
            FROM = 'XXXXXXXXXXXX@gmail.com'
            TO = ['recipient@example.com']
            SUBJECT = "FCS power capacity has dipped below 100"
            TEXT = "The Fort Calhoun Nuclear Station is at " + fcs + "%, according to the NRC: http://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/ps.html"

            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                server.close()
                print 'Sent!'
            except:
                print "Failed!"

# if plant dips below 100%, email me
if fcs < 100:
    send_email()

# tweet current status

apmonths = ["Jan.","Feb.","March","April","May","June","July","Aug.","Sept.","Oct.","Nov.","Dec."]

day = int(time.strftime("%d"))
month = int(time.strftime("%m")) - 1

OAUTH_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
OAUTH_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

text = apmonths[month] + " " + str(day) + ": The Fort Calhoun Nuclear Station is at " + fcs + "% capacity today, according to the NRC: http://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/ps.html"

t.statuses.update(status=text)