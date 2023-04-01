import feedparser,time

URL="http://un-lazy-midnight.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_NUM = 5
markdown_text="""
## 💎 Latest Blog Posts

"""  # list of blog posts will be appended here


for idx, feed in enumerate(RSS_FEED['entries']):
  if idx > MAX_NUM:
     break
  feed_date = feed['published_parsed']
  markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

with open("README.md",'r+') as f:
    content = f.read()
    new_content =  content + markdown_text
    f.seek(0)
    f.write(new_content)
    f.truncate()
