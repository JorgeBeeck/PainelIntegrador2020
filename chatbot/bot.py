from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer

# criando um novo chat bot, com o nome TOM

chatbot= ChatBot('TOM')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.portuguese')

while True:
    request = input('você: ')
    response = chatbot.get_response(request)
    print('Bot: ', response)