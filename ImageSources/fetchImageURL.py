import urllib2
from bs4 import BeautifulSoup

url = "https://morguefile.com/search/morguefile/1/%23christmas/pop"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)
print soup.prettify()