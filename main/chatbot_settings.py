from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from .interest_adapter import InterestAdapter
from .year_adapter import YearAdapter
from .language_adapter import LanguageAdapter
import os



chatbot = ChatBot(
    'Pathfinder',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'main.interest_adapter.InterestAdapter'
        },
        {
            'import_path': 'main.year_adapter.YearAdapter'
        },
        {
            'import_path': 'main.language_adapter.LanguageAdapter'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. Please refer to <a href="https://www.qub.ac.uk/directorates/InformationServices/Student/" target="_blank">Student Help</a> for assistance.',
            'maximum_similarity_threshold': 0.9
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

trainer = ChatterBotCorpusTrainer(chatbot)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(ROOT_DIR, 'data/my_corpus.yml')

# Train the chatbot with the English corpus
#trainer.train("chatterbot.corpus.english")
#trainer.train("chatterbot.corpus.english.greetings")

# Error handling
try:
    trainer.train(DATASET_PATH)
except Exception as e:
    print(f"Error during training: {e}")


def get_response(msg):
    msg_lowercase = msg.lower()
    response = str(chatbot.get_response(msg_lowercase)) 
    if not response or response == "None":
        return 'I am sorry, but I do not understand. Please refer to <a href="https://www.qub.ac.uk/directorates/InformationServices/Student/" target="_blank">Student Help</a> for assistance.'
    return response

