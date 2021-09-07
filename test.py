from translate import Translator
translator= Translator(to_lang="vi")
translation = translator.translate("This is a pen.")
print(translation)