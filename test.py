from parse import Page

local_page22 = """
<html>
<head>
    <title>The Dormouse's story</title>
</head>

<body>

<p class="title">
    <b>The Dormouse's story</b>
</p>

<p class="x3story">
    Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie
        <p class="x3">       <meta /> XXX</p>
        </a>;
    and they lived at the bottom of a well.
</p>

<p class="story">.div.p.</p>

<div class="first-iv">
    first div content
</div>

<div>
    checkmogush rayon
    <div>additional text</div>
    <p>Кое какой текстик здесь</p>
</div>
<div class="blocks">
    <div>first</div>
    <div>second</div>
    <div>third</div>
</div>

</body>
</html>

"""


lenta = Page('https://lenta.ru/news/2022/08/01/monkeypox/', 'div', 'topic-body')
mos_lenta = Page('https://moslenta.ru/news/lyudi/formula-poleznogo-zavtraka-01-08-2022.htm', 'div', '_39FNd9SD')
interfax = Page('https://www.interfax.ru/russia/855185', 'p', '')
aif = Page('https://aif.ru/sport/football/spartak_na_svoem_pole_razgromil_orenburg', 'section', 'article')
ria = Page('https://ria.ru/20220802/kulikovo_pole-1806469827.html', 'div', 'article__text')

# приходит некорректный html  -   tass
tass = Page('https://tass.ru/mezhdunarodnaya-panorama/15368327', 'p')
tass.execute()


f = interfax.reduce_comments(interfax.page)
f = interfax.keep_body(f)
f = interfax.reduce_certain_tags(f, 'script')
f = interfax.reduce_certain_tags(f, 'style')
f = interfax.reduce_singe_tags(f)
# print(f)

