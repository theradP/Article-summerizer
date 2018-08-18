feed_xml = urllib2.urlopen('http://feeds.bbci.co.uk/news/rss.xml').read()
feed = BeautifulSoup(feed_xml.decode('utf8'))
to_summarize = map(lambda p: p.text, feed.find_all('guid'))

fs = FrequencySummarizer()
for article_url in to_summarize[:5]:
  title, text = get_only_text(article_url)
  print '----------------------------------'
  print title
  for s in fs.summarize(text, 2):
   print '*',s