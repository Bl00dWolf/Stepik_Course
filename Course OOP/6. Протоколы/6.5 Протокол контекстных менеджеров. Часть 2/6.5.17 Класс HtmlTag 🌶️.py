class HtmlTag:
    def __init__(self, tag, inline=False):
        self._tag = tag
        self._level = 0
        self._content = ''
        self._indent_size = 2
        self._inline = inline

    def print(self, content):
        if not self._inline:
            indent = ' ' * self._level * self._indent_size
            lines = content.splitlines()
            for line in lines:
                print(f'{indent}{line}')
        else:
            print(content)

    def __enter__(self):
        print(f"{' ' * self._level * self._indent_size}<{self._tag}>")
        self._level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._level -= 1
        indent = ' ' * self._level * self._indent_size
        print(f'{indent}</{self._tag}>')

with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')