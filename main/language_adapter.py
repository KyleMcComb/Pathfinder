from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
from langdetect import detect, DetectorFactory, LangDetectException

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
            "yo": ["bawo", "kilo", "pele"],
        }

    def can_process(self, statement):
        return True

    def detect_language_based_on_greetings(self, message):
        words = message.lower().split()
        for lang, greet_list in self.greetings.items():
            for greet in greet_list:
                if greet in words:
                    return lang
        return None

    def process(self, input_statement, additional_response_selection_parameters=None):
        statement_text = input_statement.text.strip()

        # Check if the text is too short or includes numbers
        if len(statement_text) < 3 or statement_text.isdigit():
            return Statement("I am sorry, but I do not understand.", confidence=0.5)

        detected_language = self.detect_language_based_on_greetings(statement_text)
        if not detected_language:  # If the language isn't detected based on greetings
            try:
                detected_language = detect(statement_text)
            except LangDetectException:
                return Statement("I am sorry, but I do not understand.", confidence=0.5)

        base_url = "https://translate.google.com/?sl={}&tl=en"

        language_responses = {
            'en': None,
            'es': f"Lo siento, este chatbot solo admite inglés. Por favor, use <a href='{base_url.format('es')}' target='_blank'>Google Translate</a> para comunicarse en inglés.",
            'fr': f"Désolé, ce chatbot ne prend en charge que l'anglais. Veuillez utiliser <a href='{base_url.format('fr')}' target='_blank'>Google Translate</a> pour communiquer en anglais.",
            'de': f"Entschuldigung, dieser Chatbot unterstützt nur Englisch. Bitte verwenden Sie <a href='{base_url.format('de')}' target='_blank'>Google Translate</a> um auf Englisch zu kommunizieren.",
            'zh-cn': f"对不起，此聊天机器人仅支持英语。 请使用<a href='{base_url.format('zh-CN')}' target='_blank'>Google翻译</a>与英文交流。",
            'zh-tw': f"對不起，此聊天機器人僅支持英語。 請使用<a href='{base_url.format('zh-TW')}' target='_blank'>Google翻譯</a>與英文交流。",
            'ms': f"Maaf, chatbot ini hanya menyokong Bahasa Inggeris. Sila gunakan <a href='{base_url.format('ms')}' target='_blank'>Google Translate</a> untuk berkomunikasi dalam Bahasa Inggeris.",
            'ur': f"معاف کیجئے، یہ چیٹ بوٹ صرف انگریزی زبان کو مدعو کرتا ہے۔ براہ کرم <a href='{base_url.format('ur')}' target='_blank'>گوگل ترجمہ</a> استعمال کریں۔",
            'hi': f"मुझे खेद है, यह चैटबॉट केवल अंग्रेजी समर्थन करता है। कृपया <a href='{base_url.format('hi')}' target='_blank'>Google अनुवाद</a> का उपयोग करें।",
            'yo': f"Mo dupe, chatbot yii ṣe aṣaọkan gege bi English nikan. Jowo lo <a href='{base_url.format('yo')}' target='_blank'>Google Translate</a> lati sọrọ ni ede Geesi.",
            'bn': f"দুঃখিত, এই চ্যাটবটটি কেবল ইংরেজি সমর্থন করে। দয়া করে <a href='{base_url.format('bn')}' target='_blank'>Google অনুবাদ</a> ব্যবহার করতে ইংরেজিতে যোগাযোগ করুন।",
            'it': f"Mi dispiace, questo chatbot supporta solo l'inglese. Si prega di utilizzare <a href='{base_url.format('it')}' target='_blank'>Google Translate</a> per comunicare in inglese."
        }

        response_text = language_responses.get(detected_language, f"Sorry, this chatbot only supports English. Please use <a href='https://translate.google.com/' target='_blank'>Google Translate</a> to communicate in English.")
        print(f"Chosen response: {response_text}")  # Print the chosen response before returning

        if response_text is None:  # English detected, let other adapters handle it
            return Statement("", confidence=0)
        else:
            confidence = 0.8
            return Statement(response_text, confidence=confidence)
