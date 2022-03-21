'''
This module calls the Language Translator AI Service in IBM Cloud
to translate English text to French and vice versa
'''
#import json

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url(url)

# languages = language_translator.list_identifiable_languages().get_result()
# print(json.dumps(languages, indent=2))

def english_to_french(english_text):
    """ translate english to french """
    translation = language_translator.translate(
    text = english_text,
    model_id = 'en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """ translate french to english """
    translation = language_translator.translate(
    text = french_text,
    model_id = 'fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text

english = french_to_english('Bonjour')
print("French 'Bonjour' translated to English is ", english)

english = french_to_english("C'est ma maison")
print('French ', "C'est ma maison", ' translated to English is ', english)

english = french_to_english('Ravi de vous rencontrer')
print("French 'Ravi de vous rencontrer' translated to English is ", english)

french = english_to_french('Hello')
print("English 'Hello' translated to French is ", french)

french = english_to_french('This is my house')
print("English 'This is my house' translated to French is ", french)

french = english_to_french('Nice to meet you')
print("English 'Nice to meet you' translated to French is ", french)