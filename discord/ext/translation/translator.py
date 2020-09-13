
class Translator:
    def __init__(self, language, locale):
        self.language = language

        if hasattr(locale, 'locale'):
            self.locale = locale.locale
        else:
            self.locale = locale

    async def lang(self, path, values={}):
        keys = path.split('|')

        try:
            string = self.language.strings[self.locale]
            for key in keys:
                string = string[key]
        except KeyError:
            if self.locale == self.language.source:
                return
            try:
                string = self.language.strings[self.language.source]
                for key in keys:
                    string = string[key]
            except KeyError:
                return

        if values:
            return string.format(**values)

        return string
