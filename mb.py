import urllib2
from bs4 import BeautifulSoup

next_flag = True

n = 1

while next_flag:
  soup = BeautifulSoup(urllib2.urlopen('http://www.mb.com.ph/category/news/national/page/%d/' % n))

  for post in soup.find_all('div', class_='post'):
    date = post.find('span', class_='meta_date').contents[0].split()
    month = date[0]
    year = date[2]
    link = post.p.a.get('href')

    if year == "2013":
      try:
        print "%s, %s" % (month, link)
      except Exception as ex:
        pass
    else:
      next_flag = False

  n += 1