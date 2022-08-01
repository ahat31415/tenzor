# import re
#
# txt =  "Sylvie is 20 years old."
#
# # Регулярное выражение для извлечения чисел из строки <div*.class="*\w">
# age = re.findall(r'<a*\wid="link\d">*\w</a>', page)
#
# print(age)
import requests

url = 'https://moslenta.ru/news/lyudi/formula-poleznogo-zavtraka-01-08-2022.htm'
url = 'https://lenta.ru/news/2022/08/01/monkeypox/'

mypage2 = requests.get(url).text
# print(page)
mypage = """
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

<div class="first-div">
    first div content
</div>

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


class Page:
    def __init__(self, url1):
        self.url = url1


def find_all(page, tagName):
    index = 0
    while index < len(page):
        insideTag = False
        if page[index] == '<':
            index += 1
            substr = ''
            while page[index] != '>':
                substr += page[index]
                index += 1
            # now we are at the '>' symbol
            index += 1
            if tagName in substr:
            # if True:
                print(substr)
                insideTag = True
        else:
            index += 1


        if insideTag:
            tagContent = ''
            closeTag = f'</{tagName}>'
            while closeTag not in page[index: index + len(closeTag)] :
                tagContent += page[index]
                index += 1
            print(f'---------------------------')
            print(f'{tagContent}')
            print(f'---------------------------')


find_all(mypage, 'div')


