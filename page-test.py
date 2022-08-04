def reduce_singe_tags(page):
    single_tags = [
        '<!doctype',
        '<area',
        '<base',
        '<br',
        '<col',
        '<embed',
        '<hr',
        '<img',
        '<input',
        '<keygen',
        '<link',
        '<meta',
        '<param',
        '<source',
        '<track',
        '<wbr',
    ]
    # index = page.index('<body')
    index = 0
    temp_page = page[index: len(page)]
    for tag in single_tags:
        while tag in temp_page:
            start = temp_page.index(tag)
            print(f'start:{start}')
            end = temp_page.index('>', start)
            print(f'end:{end}')
            temp_page = temp_page[0:start] + temp_page[end + 1:]
    return temp_page


def reduce_scripts(page):
    temp_page = page
    while '<script' in temp_page:
        start = temp_page.index('<script')
        print(f'start:{start}')
        end = temp_page.index('</script>', start) # </script>
        print(f'end:{end}')
        temp_page = temp_page[0:start] + temp_page[end + 10:]
    return temp_page


def keep_body(page):

    temp_page = page
    if '<body' in temp_page:
        start = temp_page.index('<body')
        end_of_body_open = temp_page.index('>', start) + 1
        print('end_of_body_open')
        print(end_of_body_open)
        print(temp_page[end_of_body_open])
        end = temp_page.index('</body>', end_of_body_open)
        temp_page = temp_page[end_of_body_open:end]
    return temp_page











p = '<p class="x3">%<meta />% XXX</p>'
w=  '0123456789012345678901234567890'
p2 = """
<html>
<head>

    <link href="title.css" rel="stylesheet" type="text/css" />
    <link href="title.css" rel="stylesheet" type="text/css" />
    <link href="title.css" rel="stylesheet" type="text/css" />
    <link href="title.css" rel="stylesheet" type="text/css" />

    <title>The Dormouse's story</title>
</head>
before body begin
<body data-pagetype="content_1448">
after body begin
<p class="title">
    <b>The Dormouse's story</b>
</p>

<img src="https://top-fwz1.mail.ru/counter?id=59428;js=na" style="border:0;position:absolute;left:-9999px;" alt="Top.Mail.Ru" />
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
<img src="https://top-fwz1.mail.ru/counter?id=59428;js=na" style="border:0;position:absolute;left:-9999px;" alt="Top.Mail.Ru" />
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
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width,initial-scale=1">
before body end
</body>
afterbodyend
1-----
<script>
><><><><><><>////><><?<//>
</script>
2-----
</html>

"""
page = keep_body(p2)
# page = reduce_scripts(page)
# page = reduce_singe_tags(page)

print(page)