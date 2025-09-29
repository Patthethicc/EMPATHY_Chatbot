from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy

spacy.load('en_core_web_sm')
chatbot = ChatBot("Rainier")

trainer = ListTrainer(chatbot)

trainer.train([
    "Let's go !",
    "That's great to hear ! Tell me more about it.",
])

trainer.train([
    "I'm so annoyed right now !",
    "I'm sorry to hear that you're annoyed, take a breather first ",
])

trainer.train([
    "Man today sucks...",
    "It's alright, things happen from time to time, would you like to talk about why today sucks?",
])

print('Type something...')

while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(f"{chatbot.name}: {bot_response}")

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break