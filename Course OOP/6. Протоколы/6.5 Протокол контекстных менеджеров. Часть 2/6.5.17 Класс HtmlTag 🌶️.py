class HtmlTag:
    level = 0

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        self.__class__.level += 1
        print(f'{"  " * (self.__class__.level - 1)}<{self.tag}>', end='')
        if not self.inline:
            print()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.inline:
            print(f'{"  " * (self.__class__.level - 1)}', end='')
        print(f'</{self.tag}>')
        self.__class__.level -= 1

    def print(self, content):
        if self.inline:
            print(content, end='')
        else:
            print(f'{"  " * self.__class__.level}{content}')


with HtmlTag('body') as _:
    with HtmlTag('h1', True) as header:
        header.print('Поколение Python')
    with HtmlTag('p', True) as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')
