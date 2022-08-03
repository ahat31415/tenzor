import requests

local_page = """
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


class Page:

    def __init__(self, url_, tag_name: str, css_class: str = ''):
        # self.page = requests.get(url_).text
        self.page = local_page
        self.tag_name = tag_name
        self.css_class = css_class

    def return_inner(self, index: int):

        opened_tags_counter = 0
        tag_content = ''
        close_tag = f'</{self.tag_name}>'
        while index < len(self.page) - 1 and \
                (
                        close_tag not in self.page[index: index + len(close_tag)] or \
                        close_tag in self.page[index: index + len(close_tag)] and opened_tags_counter != 0
                ):

            char = self.page[index]
            char2 = self.page[index + 1]
            if char == '<' and char2 != '/':
                opened_tags_counter += 1
            if char == '<' and char2 == '/':
                opened_tags_counter -= 1
            tag_content += char
            index += 1
        # print(f'closeTag внутри -> ({page[index: index + len(closeTag)]})')
        index += len(close_tag)
        # print(f'-- Содержимое ниже ------------------------- index={index}')
        # print(f'{tagContent}')
        # print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        return tag_content, index

    def find_all(self, page: str, tag_name: str = ''):
        if tag_name == '':
            index = 0
        else:
            index = page.index('body')
        result = []
        string_buffer = ''
        while index < len(page):
            if page[index] == '<':
                #  определяем одиночный тег -------------
                close_tag_index = page.index('>', index)
                _close_tag = page[close_tag_index - 1]
                if (_close_tag == '/'):
                    print(f'одиночный тег |{page[index: close_tag_index + 1]}|')
                    index = close_tag_index + 1
                    print(f'|{page[index]}|')
                    # continue
                # ---------------------------------------
                index += 1
                tag_content = ''
                while page[index] != '>':
                    tag_content += page[index]
                    index += 1
                    if index >= len(page):
                        break

                index += 1  # we are at the '>' symbol therefore +1 to the next char
                splitted_tag_content = tag_content.split(' ')
                class_condition = self.is_class_condition(tag_content)
                if tag_name in splitted_tag_content and tag_name != '' and class_condition:  # tag_name != '' ??
                    # print(substr)
                    tag_inner_text, index = self.return_inner(index)
                    tag_inner_text = self.href_handling(tag_inner_text)
                    result += self.find_all(tag_inner_text)
                    # result.append(tag_inner_text)
                elif tag_name == '':
                    result.append(string_buffer)
                    string_buffer = ''
            else:
                string_buffer += page[index]
                index += 1
        if tag_name == '':
            result.append(string_buffer)
        return result

    def href_handling(self, text):
        try:
            if '<a ' not in text:
                return text

            start = text.index('<a ', 0)
            end = text.index('</a>', 0)

            index = start + 3

            a_tag_content = ''
            while text[index] != '>':
                a_tag_content += text[index]
                index += 1
            index += 1

            href_index = a_tag_content.index('href="') + 6
            href_index_end = a_tag_content.index('"', href_index)
            href = a_tag_content[href_index:href_index_end]
            a_text = ''
            while index < end:
                a_text += text[index]
                index += 1
            a_text += f'[{href}]'

            index += 1  # we are at the '>' symbol therefore +1 to the next char
            replace_this = text[start: end + 4]
            fine_text = text.replace(replace_this, a_text)
            return self.href_handling(fine_text)
        except:
            print('exception text')
            print(text)
            raise Exception

    def is_class_condition(self, st):
        elems = st.split('"')
        for index, el in enumerate(elems):
            if 'class=' in el and index != len(elems):
                classes = elems[index + 1].split(' ')
                if f'{self.css_class}' in classes:
                    print('--------------------------------------------------------------------------')
                    print(f'classes is {classes}')
                    return True
        return False

    def execute(self):
        for l in self.find_all(self.page, self.tag_name):
            line = l.strip()
            if line != '':
                print('')
                print(line)


local_page = Page(local_page, 'p', 'x3')
lenta = Page('https://lenta.ru/news/2022/08/01/monkeypox/', 'div', 'topic-body')
# lenta = Page('https://lenta.ru/news/2022/08/01/monkeypox/', 'p', 'xsdcmg topic-body _news')
mos_lenta = Page('https://moslenta.ru/news/lyudi/formula-poleznogo-zavtraka-01-08-2022.htm', 'p')
aif = Page('https://aif.ru/sport/football/spartak_na_svoem_pole_razgromil_orenburg', 'p')
ria = Page('https://ria.ru/20220802/kulikovo_pole-1806469827.html', 'div')

# приходит некорректный html  -   tass
tass = Page('https://tass.ru/mezhdunarodnaya-panorama/15368327', 'p')

# print(ria.page)
local_page.execute()

# a = ''
# if a in 'asd asd asddasd' and a != '':
#     print('1')
# elif a == '':
#     print('2')
