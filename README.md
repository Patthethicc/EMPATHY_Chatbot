# EMPATHY_Chatbot
Chatbot for our Empathy subject

## Setup
1. Clone the repository, then change it to its directory
```bash
git clone https://github.com/Patthethicc/EMPATHY_Chatbot.git
```
2. Install the needed libraries
```bash
pip install chatterbot
python -m spacy download en_core_web_sm
```
3. In the directory, run this command to use the chatbot in the terminal
```bash
python -u "bot.py"
```
Note: to exit the bot, do ctrl + c or ctrl + d

## How to train the bot?
1.Add a conversation here inside trainer.train

Example:
```bash
trainer.train([
    "Hi Rainier the bot, how are you?", #<-- User Input
    "I'm doing good, how about you?", #<--Bot response
    "Doing neat as well, have a great day !", #<-- User Input
    "Alright, have a good one !" #<--Bot response
])
#Possible vice versa as well
```
2. Run "bot.py" and then converse the bot with the full sentences or phrases inside the List to guide the bot

##Documentation of chatterbot
```bash
https://docs.chatterbot.us/tutorial
```
