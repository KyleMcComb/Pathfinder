from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from langdetect import detect, DetectorFactory

# Set a deterministic seed for langdetect
DetectorFactory.seed = 0

class LanguageAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

        self.greetings = {
            "en": ["hello", "hi", "hey", "yo"],
            "de": ["hallo", "hi", "grüße", "moin"],
            "es": ["hola", "ola", "oye", "ei"],
            "zh-cn": ["你好", "早", "嗨"],
            "fr": ["salut", "bonjour", "coucou", "allo"],
            "it": ["ciao", "salve", "ehi"],
            "bn": ["নমস্কার", "হ্যালো"],
            "ms": ["hello", "hai", "selamat pagi"],
            "ur": ["سلام", "ہیلو", "ہائے"],
            "hi": ["नमस्ते", "हैलो", "हाय"],
        }

    def can_process(self, statement):
        # We are attempting to handle all languages, so we'll always return True here
        return True

    def detect_language_based_on_greetings(self, message):
        words = message.lower().split()
        for lang, greet_list in self.greetings.items():
            for greet in greet_list:
                if greet in words:
                    return lang
        return None

    def process(self, input_statement, additional_response_selection_parameters=None):
        detected_language = self.detect_language_based_on_greetings(input_statement.text)
        if not detected_language:  # If the language isn't detected based on greetings
            detected_language = detect(input_statement.text)

        language_responses = {
            'en': None,
            'es': "Lo siento, este chatbot solo admite inglés. Por favor, use Google Translate para comunicarse en inglés.",
            'fr': "Désolé, ce chatbot ne prend en charge que l'anglais. Veuillez utiliser Google Translate pour communiquer en anglais.",
            'de': "Entschuldigung, dieser Chatbot unterstützt nur Englisch. Bitte verwenden Sie Google Translate, um auf Englisch zu kommunizieren.",
            'zh-cn': "对不起，此聊天机器人仅支持英语。 请使用Google翻译与英文交流。",
            'zh-tw': "對不起，此聊天機器人僅支持英語。 請使用Google翻譯與英文交流。",
            'ms': "Maaf, chatbot ini hanya menyokong Bahasa Inggeris. Sila gunakan Google Translate untuk berkomunikasi dalam Bahasa Inggeris.",
            'ur': "معاف کیجئے، یہ چیٹ بوٹ صرف انگریزی زبان کو مدعو کرتا ہے۔ براہ کرم انگریزی میں بات چیت کے لئے گوگل ترجمہ استعمال کریں۔"
        }

        response_text = language_responses.get(detected_language, "Sorry, this chatbot only supports English. Please use Google Translate to communicate in English.")
        print(f"Chosen response: {response_text}")  # Print the chosen response before returning

        if response_text is None:  # English detected, let other adapters handle it
            return Statement("", confidence=0)
        else:
            confidence = 0.8
            return Statement(response_text, confidence=confidence)
