from parse import Page



import sys
import click

@click.command()
@click.argument('url')
def main(url):
    file = open('settings.txt', 'r')
    lines = []
    try:
        for line in file:
            lines.append(line)
    finally:
        file.close()

    # url = lines[0].replace('\n', '')
    tag_name = ''
    css_class = ''
    try:
        tag_name = lines[0].replace('\n', '')
        css_class = lines[1].replace('\n', '')
    except:
        pass
    Page(url, tag_name, css_class).execute()
    # print(f'$${url}$$')
    # print(f'$${tag_name}$$')
    # print(f'$${css_class}$$')
    pass


if __name__ == '__main__':
    main()
