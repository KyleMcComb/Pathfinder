from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

chatbot = ChatBot('Pathfinder')

trainer = ChatterBotCorpusTrainer(chatbot)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(ROOT_DIR, 'data\my_corpus.yml')

# Train the chatbot with the English corpus
#trainer.train("chatterbot.corpus.english")
#trainer.train("chatterbot.corpus.english.greetings")

# Error handling
try:
    trainer.train(DATASET_PATH)
except Exception as e:
    print(f"Error during training: {e}")

def get_response(msg):
    msg_lowercase = msg.lower() # Code to convert user response to lowercase
    return str(chatbot.get_response(msg_lowercase))


