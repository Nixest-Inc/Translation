import re
from json import load as to_json
from os import listdir
from .translator import Translator

class Files:
    def __init__(self, source, path='./json/translate/', file_extension='json'):
        self.source = source
        self.path = path
        self.file_ext_len = len(file_extension) + 1
        self.strings = {}

    async def load_translations(self, locale, path=None):
        if path is None:
            path = self.path + locale + '/'

        strings = {}

        for file_name in listdir(path):
            with open(path + file_name, encoding='utf-8') as file:
                strings[file_name[:-self.file_ext_len]] = to_json(file)

        self.strings[locale] = strings

    async def load_languages(self, path=None, pattern='^[a-z]{2}((_|-)[A-Z]{2})?$'):
        if path is None:
            path = self.path

        pattern = re.compile(pattern)
        for locale in [locale for locale in listdir(path) if pattern.match(locale)]:
           await self.load_translations(locale, path + locale + '/')

    async def get(self, locale):
        translation = Translator(self, locale)
        return translation.lang