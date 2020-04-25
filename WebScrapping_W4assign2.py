from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
l=[]
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
pos=17
tags = soup('a')
link=tags[pos].get('href',None)
print(tags[pos].contents[0])
for i in range(18,24):
         html = urlopen(link, context=ctx).read()
         soup = BeautifulSoup(html, 'html.parser')
         tags = soup('a')
         link = tags[pos].get('href', None)
         print(tags[pos].contents[0])
         #print("2   ",link)


#print(tag.get('href',None))
#print(a)
