import feedparser, time

URL="https://v2.velog.io/rss/bbatto5302"
RSS_FEED = feedparser.parse(URL)
MAX_POST=5

markdown_text = """
<div align="center">
  
  <h2>프론트엔드 개발자, 배창현 입니다.
<img src="https://camo.githubusercontent.com/e8e7b06ecf583bc040eb60e44eb5b8e0ecc5421320a92929ce21522dbc34c891/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f6876524a434c467a6361737252346961377a2f67697068792e676966" width="35" data-canonical-src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" style="max-width: 100%;">
 </h2>
  
  [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fbaechanghyeon&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com) 
<br>  

## 🛠 Tech Stack
<img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML5&logoColor=white">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white">  
<img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=React&logoColor=white"> 
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"> 
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=TypeScript&logoColor=white"> <br>
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=white">
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white">
<img src="https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=Figma&logoColor=white">
<img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=Notion&logoColor=white"> <br>
<img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=white">
<img src="https://img.shields.io/badge/Bulma-00D1B2?style=flat-square&logo=Bulma&logoColor=white"> <br>
<br>
  
</div>

### 📕 Latest Blog Posts </h3> 
""" # list of blog posts will be appended here


for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
