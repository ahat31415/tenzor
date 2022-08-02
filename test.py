page = """111<div>000</div>333</div>"""

index = 0
tagName = 'div'
openedTagsCounter = 0
tagContent = ''
closeTag = f'</{tagName}>'

while index < len(page) - 1 and \
        (
                closeTag not in page[index: index + len(closeTag)] or \
                closeTag in page[index: index + len(closeTag)] and openedTagsCounter != 0
        ):

    char = page[index]
    char2 = page[index + 1]
    if char == '<' and char2 != '/':
        openedTagsCounter += 1
        print(f'at the increasing: index={index} char={char} char2={char2}')
    if char == '<' and char2 == '/':
        openedTagsCounter -= 1
        print(f'at the decreasing: index={index} char={char} char2={char2}')
    tagContent += char
    index += 1
print(f'closeTag внутри -> {page[index: index + len(closeTag)]}')
print(f'-- Содержимое ниже ------------------------- index={index}')
print(f'{tagContent}')
print(f'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

print(openedTagsCounter)