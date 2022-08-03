def find_all(page: str, tag_name: str = ''):
    # index = page.index('body')
    index = 0
    result = []
    string_buffer = ''
    while index < len(page):
        if page[index] == '<':
            index += 1
            substr = ''
            while page[index] != '>':
                substr += page[index]
                index += 1
            index += 1  # we are at the '>' symbol therefore +1 to the next char
            current_tag = substr.split(' ')
            if tag_name in current_tag:
                # print(substr)
                tag_content = page
                result += find_all(tag_content)
            elif tag_name == '':
                result.append(string_buffer)
                string_buffer = ''
        else:
            string_buffer += page[index]
            index += 1
    if tag_name == '':
        result.append(string_buffer)

    return result


page = """

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

<p class="story">.div.p.</p>

<div class="first-iv">
    first div content
</div>"""

f = """
<b class="abcd">The Dormouse\'s story</b>
Once upon a time there were three little sisters; and their names were 
       <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a> 
        ,fdasdfasf  
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and  
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
        dgdfghdfghdfghhfg    
        and they lived at the bottom of a well
        ..div.p.  Кое какой текстик здесь
        """


# for i in find_all(f, ''):
#     print(i.strip())

def href_handling(text):
    if '<a ' not in text:
        return text

    start = text.index('<a ', 0)
    end = text.index('</a>', 0)

    index = start + 3
    print(f'start = {start}')
    print(f'end = {end}')
    print(f'text[index] = {text[index]}')

    a_tag_content = ''
    while text[index] != '>':
        a_tag_content += text[index]
        index += 1
    index += 1

    href_index = a_tag_content.index('href="') + 6
    href_index_end = a_tag_content.index('"', href_index)
    href = a_tag_content[href_index:href_index_end]
    print(f'href = {href}')
    a_text = ''
    while index < end:
        a_text += text[index]
        index += 1
    a_text += f'[{href}]'
    print(f'a_text = {a_text}')

    index += 1  # we are at the '>' symbol therefore +1 to the next char
    replace_this = text[start: end + 4]
    print(replace_this)
    fine_text = text.replace(replace_this, a_text)
    return href_handling(fine_text)


ss2 = ' 1123 <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a> 123 <a class="sister" id="link1" href="http://vk.com/rwfW@fwe">Click here</a>'
a = ''
tutu = href_handling(ss2)
print('tutu')
print(tutu)
