import os
import requests


class Page:

    def __init__(self, url_, tag_name: str, css_class: str = ''):
        self.url_ = url_
        self.page = requests.get(url_).text
        # self.page = url_
        self.tag_name = tag_name
        self.css_class = css_class
        print('constructor')
        print(f'aa{self.url_}aa')
        # print(self.page)
        print(f'aa{self.tag_name}aa')
        print(f'aa{self.css_class}aa')

    @staticmethod
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
                # print(f'start:{start}')
                end = temp_page.index('>', start)
                # print(f'end:{end}')
                temp_page = temp_page[0:start] + temp_page[end + 1:]
        return temp_page

    @staticmethod
    def reduce_certain_tags(page, removing_tag_name):
        print(removing_tag_name)
        temp_page = page
        while f'<{removing_tag_name}' in temp_page:
            start = temp_page.index(f'<{removing_tag_name}')
            end = temp_page.index(f'</{removing_tag_name}>', start)  # </script>
            # print(f'start:{start}')
            # print(f'end:{end}')
            temp_page = temp_page[0:start] + temp_page[end + len(removing_tag_name)+3:]  # раньше было просто 10 для </script>
        return temp_page

    @staticmethod
    def keep_body(page):

        temp_page = page
        if '<body' in temp_page:
            try:
                start = temp_page.index('<body')
                end_of_body_open = temp_page.index('>', start) + 1
                # print('end_of_body_open')
                # print(end_of_body_open)
                # print(temp_page[end_of_body_open])
                end = temp_page.index('</body>', end_of_body_open)
                temp_page = temp_page[end_of_body_open:end]
            except ValueError:
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print('Keep body Value Error happened!')
                return page
        return temp_page

    @staticmethod
    def reduce_comments(page):
        temp_page = page
        while f'<!--' in temp_page:
            start = temp_page.index(f'<!--')
            end = temp_page.index(f'-->', start)  # </script>
            # print(f'start:{start}')
            # print(f'end:{end}')
            temp_page = temp_page[0:start] + temp_page[end + 4:]
        return temp_page


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
                #  определяем одиночный тег -------------
                try:
                    close_tag_index = self.page.index('>', index)
                    # print(f'index = {close_tag_index}')
                    _close_tag = self.page[close_tag_index - 1]
                    if (_close_tag == '/'):
                        # print(f'char = {char} Одиночный тег |{self.page[index: close_tag_index + 1]}|')
                        index = close_tag_index + 1
                        # print(f'|{self.page[index]}|')
                        continue
                    else:
                        opened_tags_counter += 1
                except ValueError as err:
                    # print(err)
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
        index = 0
        # if tag_name == '':
        #     index = 0
        # else:
        #     index = page.index('body')
        result = []
        string_buffer = ''
        while index < len(page):
            if page[index] == '<':
                #  определяем одиночный тег -------------
                # close_tag_index = page.index('>', index)
                # _close_tag = page[close_tag_index - 1]
                # if (_close_tag == '/'):
                #     print(f'одиночный тег |{page[index: close_tag_index + 1]}|')
                #     index = close_tag_index + 1
                #     print(f'|{page[index]}|')
                #     # continue
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
            print('exception text >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            print(text)
            return text
            # raise Exception

    def is_class_condition(self, st):
        if self.css_class == '':
            return True
        elems = st.split('"')
        for index, el in enumerate(elems):
            if 'class=' in el and index < len(elems) - 1:
                classes = elems[index + 1].split(' ')
                if f'{self.css_class}' in classes:
                    # print('--------------------------------------------------------------------------')
                    # print(f'classes is {classes}')
                    return True
        return False

    def execute(self):
        refined_page = self.reduce_comments(self.page)

        refined_page = self.keep_body(refined_page)
        refined_page = self.reduce_certain_tags(refined_page, 'script')
        refined_page = self.reduce_certain_tags(refined_page, 'style')
        refined_page = self.reduce_singe_tags(refined_page)
        self.page = refined_page

        # refined_page = self.page
        # refined_page = self.keep_body(self.page)
        # refined_page = self.reduce_scripts(self.page)
        # refined_page = self.reduce_singe_tags(self.page)
        result = self.find_all(self.page, self.tag_name)
        slashes_index = self.url_.index('//') + 2
        tutu = self.url_[slashes_index:].replace('.html', '')
        cur_dir = os.getcwd().replace(':', '')
        file_name = cur_dir + f'-{tutu}.txt'
        file_name = file_name.replace('/', '-')
        file_name = file_name.replace('\\', '-')
        print(file_name)
        file = open(file_name, 'w')
        try:
            for l in result:
                line = l.strip()
                if line != '':
                    line = self.format_long_text(line)
                    file.write('\n')
                    file.write('\n')
                    file.write(line)
                    # print('')
                    # print(line)
        finally:
            file.close()
        print(f'Выполнено. Имя файла: {file_name}')

    @staticmethod
    def format_long_text(text):
        words = text.split(' ')
        buffer = ''
        new_text = ''
        for i in range(len(words)):
            if words[i] != '':
                next_word = f' {words[i]}'
                buffer += next_word
                if len(buffer) > 80:
                    buffer += '\n'
                    new_text += buffer
                    buffer = ''
        if buffer != '':
            buffer += '\n'
            new_text += buffer
        return new_text


