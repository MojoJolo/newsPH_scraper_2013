import urllib2
from bs4 import BeautifulSoup

next_flag = True

n = 1

while next_flag:
  soup = BeautifulSoup(urllib2.urlopen('http://newsinfo.inquirer.net/category/latest-stories/page/%d' % n))

  for link in soup.find_all('div', class_='post'):
    month = link.find('p', class_='metas').contents[0].split()[1]
    year = link.find('p', class_='metas').contents[0].split()[3]
    
    if year == "2013":
      print "%s, %s" % (month, link.h1.a.get('href'))
    else:
      next_flag = False

  n += 1