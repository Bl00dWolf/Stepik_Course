class TitledText(str):
    def __new__(cls, content: str, text_title: str, *args, **kwargs):
        instance = super().__new__(cls, content)
        instance._text_title = text_title
        return instance

    def title(self):
        return self._text_title
