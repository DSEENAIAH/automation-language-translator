#installing the google trans using bellow command 
#  pip install --user googletrans==4.0.0-rc1

from googletrans import Translator, LANGUAGES

# below line print the how many languages present in that googletrans.
# print(LANGUAGES)

text = "hi! how are you?"
translator = Translator()

lang = translator.detect(text).lang

#the below code will print the which language is ur sentainse present ex: hindhi, english, telugu etc..
# print(lang)
 
english_translated_text = translator.translate(text, src=lang, dest='te')
print(english_translated_text.text)
