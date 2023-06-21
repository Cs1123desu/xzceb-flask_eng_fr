"""Imports"""
from deep_translator import MyMemoryTranslator

#Translator Defintions
def english_to_french(english_text):
    """English to French"""
    
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    #translation = MyMemoryTranslator(text=english_text, model_id='en-fr').translate(english_text)
    #french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """French to English"""
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    #translation = MyMemoryTranslator(text=french_text, model_id='en-fr').translate(french_text)
    #english_text = translation['translations'][0]['translation']
    return english_text
