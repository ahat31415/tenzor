html_doc = """
<html>
<head>
    <title>The Dormouse's story</title>
</head>

<body>

<p class="title">
    <b>The Dormouse's story</b>
</p>

<p class="story">
    Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.
</p>

<p class="story">...</p>
<div>
    checkmogush rayon
    <div>additional text</div>
    <p>p text</p>
</div>
<div class="blocks">
    <div>first</div>
    <div>second</div>
    <div>third</div>
</div>

</body>
</html>

"""

from bs4 import BeautifulSoup
import requests
url = 'https://moslenta.ru/news/lyudi/formula-poleznogo-zavtraka-01-08-2022.htm'
url = 'https://lenta.ru/news/2022/08/01/monkeypox/'
page = requests.get(url).text
# soup = BeautifulSoup(html_doc, 'html.parser')
soup = BeautifulSoup(page, 'html.parser')

soup.prettify()


soup.title
# <title>The Dormouse's story</title>

soup.title.name
# u'title'

soup.title.string
# u'The Dormouse's story'

soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

soup.p['class']
# u'title'

soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print(soup.find(id="link3"))
# # print(soup.find(id="link3").text)
# print('--------------------------------')
# for div in soup.find_all('div', class_='topic-body'):
#     print(div.h1.text)
#     for p in div.find_all('p'):
#         print('')
#         print(p.text)

# print(soup.find(id="link3").text)
print('--------------------------------')
for div in soup.find_all('div'):
    print('---')
    print(div.text)
# print(soup.a['sister'])
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>