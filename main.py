import feedparser,time

URL="http://un-lazy-midnight.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_NUM = 5

markdown_text="""


![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=300&section=header&text=busymidnight&fontAlignY=40&fontSize=50&desc=🌷&descAlignY=65&animation=twinkling)

 <div align="center">
   <h3>Hello World 👋 I'm Yeonkyung</h3>
    <br>

   <h3>📚 Tech Stack 📚</h3>
  	<br>

 <p align="center">
   <img src="https://img.shields.io/badge/Java-007396?style=flat&logo=CoffeeScript&logoColor=white"></a>&nbsp 
   <img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/></a>&nbsp    
   <img src="https://img.shields.io/badge/CSharp-239120?style=flat-square&logo=CSharp&logoColor=white"/></a>&nbsp 
   <br>
   <img src="https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=Spring&logoColor=white"/></a>&nbsp 
   <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white"/></a>&nbsp 
   <!--<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/></a>&nbsp--> 
   <!--<img src="https://img.shields.io/badge/aws-333664?style=flat-square&logo=amazon-aws&logoColor=white"/></a>&nbsp--> 
   <br>
   <img src="https://img.shields.io/badge/Javascript-ffb13b?style=flat-square&logo=javascript&logoColor=white"/></a>&nbsp 
   <img src="https://img.shields.io/badge/html5-E34F26?style=flat-square&logo=html5&logoColor=white"/></a>&nbsp 
   <img src="https://img.shields.io/badge/css-1572B6?style=flat-square&logo=css3&logoColor=white"/></a>&nbsp 
   <br>
 </p>
  <br>
  <a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fbusymidnight&count_bg=%23BEBEBE&title_bg=%23FFFFFF&icon=baidu.svg&icon_color=%23726161&title=%C2%B7&edge_flat=false"/></a>
  <br>
  <img src="https://github-readme-stats.vercel.app/api?username=busymidnight&show_icons=true">
  <br>
  <br>
  </div>
 
## :mailbox_with_mail: Contacts
[![Tech Blog Badge](http://img.shields.io/badge/-Tech%20blog-black?style=flat-square&logo=tistory&link=https://un-lazy-midnight.tistory.com/)](https://un-lazy-midnight.tistory.com/)

## 🪄Latest Blog Posts 🪄

  """


for idx, feed in enumerate(RSS_FEED['entries']):
  if idx > MAX_NUM:
     break
  feed_date = feed['published']
  pubdate = time.strptime(feed_date,'%a, %d %b %Y %H:%M:%S %z')
  markdown_text += f"[{pubdate.tm_mon}/{pubdate.tm_mday} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
