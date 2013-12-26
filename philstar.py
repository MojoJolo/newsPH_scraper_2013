import urllib2
from bs4 import BeautifulSoup

next_flag = True

philstar = 'http://www.philstar.com'
n = 0

while next_flag:
  soup = BeautifulSoup(urllib2.urlopen('http://www.philstar.com/nation/archive/top-stories?page=%d' % n))

  for post in soup.find_all('tr', class_=['odd', 'even']):
    link = "%s%s" % (philstar, post.find('span', 'article-title').a.get('href'))

    date = post.find('span', 'date-display-single').contents[0].split()
    month = date[0]
    year = date[2]

    if year == "2013":
      print "%s, %s" % (month, link)
    else:
      next_flag = False

  n += 1