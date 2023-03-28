from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

chatbot = ChatBot('MyChatBot')

trainer = ChatterBotCorpusTrainer(chatbot)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(ROOT_DIR, 'data\my_corpus.yml')

# Train the chatbot with the English corpus
#trainer.train("chatterbot.corpus.english")
#trainer.train("chatterbot.corpus.english.greetings")
trainer.train(DATASET_PATH)

def get_response(msg):
    return str(chatbot.get_response(msg))