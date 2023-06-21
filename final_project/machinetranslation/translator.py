"""Imports"""
from deep_translator import MyMemoryTranslator

#Translator Defintions
def english_to_french(english_text):
    """English to French"""
    translation = MyMemoryTranslator(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """French to English"""
    translation = MyMemoryTranslator(text=french_text, model_id='en-fr').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
