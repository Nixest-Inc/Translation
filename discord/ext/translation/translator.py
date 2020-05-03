class translator:
    def __init__(self, i18n, locale):
        self.i18n = i18n

        if hasattr(locale, 'locale'):
            self.locale = locale.locale
        else:
            self.locale = locale

    def lang(self, path, values={}):
        keys = path.split('.')

        try:
            string = self.i18n.strings[self.locale]
            for key in keys:
                string = string[key]
        except KeyError:
            if self.locale == self.i18n.source:
                return
            try:
                string = self.i18n.strings[self.i18n.source]
                for key in keys:
                    string = string[key]
            except KeyError:
                return

        if values:
            return string.format(**values)

        return string
