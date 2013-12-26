import urllib2
from bs4 import BeautifulSoup

next_flag = True

rappler = "http://www.rappler.com"
n = 0

while next_flag:
  soup = BeautifulSoup(urllib2.urlopen('http://www.rappler.com/nation?start=%d' % n))

  for post in soup.find_all('div', class_='recent-post-data'):
    date = post.find('div', class_='post-item-meta').find('span', class_='date').contents[0].split()
    month = date[0]
    year = date[2]

    link = "%s%s" % (rappler, post.h4.a.get('href'))

    if year == "2013":
      print "%s, %s" % (month, link)
    else:
      next_flag = False

  n += 10