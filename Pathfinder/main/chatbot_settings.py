from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('MyChatBot')

trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot with the English corpus
#trainer.train("chatterbot.corpus.english")
#trainer.train("chatterbot.corpus.english.greetings")
trainer.train("main.data.my_corpus")

def get_response(msg):
    return str(chatbot.get_response(msg))