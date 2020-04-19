import unittest

from translator import Translator


class TestTranslator(unittest.TestCase):

    def testTranslate(self):
        translator = Translator()
        content = "我爱"
        from_lang = 'ch'
        to_lang = 'en'
        result = translator.translate(content,from_lang,to_lang)
        self.assertEqual("I love",result)
        translate = translator.translate("When writing unit tests", to_lang, from_lang)
        print(translate)