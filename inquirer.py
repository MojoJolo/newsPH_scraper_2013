import urllib2
from bs4 import BeautifulSoup

next_flag = True

soup = BeautifulSoup(urllib2.urlopen('http://newsinfo.inquirer.net/category/latest-stories/page/2').read())

while next_flag:
  for link in soup.find_all('div', class_='post'):
    month = link.find('p', class_='metas').contents[0].split()[1]
    year = link.find('p', class_='metas').contents[0].split()[3]
    
    if year == "2013":
      print "%s, %s" % (month, link.h1.a.get('href'))

  for nav in soup.find('div', class_='navigation').find_all('a'):
    if "Next Page" in nav.contents[0]:
      soup = BeautifulSoup(urllib2.urlopen(nav.get('href')))
      next_flag = True
    else:
      next_flag = False