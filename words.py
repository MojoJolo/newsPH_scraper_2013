csvs = ['result/philstar.csv_good.csv', 'result/philstar2.csv_good.csv', 'result/rappler.csv_good.csv', 'result/inquirer.csv_good.csv']
links = []

for csv in csvs:
  f = open(csv, 'r')

  for line in f:
    links.append(line.split(', ')[1].replace("\n", ""))

  f.close()

complete_words = []

for link in links:
  title = link.split('/')[-1]

  for word in title.split('-'):
    complete_words.append(word)

words = []

for word in complete_words:
  if not word in words:
    words.append(word)

for word in words:
  count = complete_words.count(word)

  print "%s, %d" % (word, count)