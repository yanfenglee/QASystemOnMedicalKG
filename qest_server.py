
from flask import Flask, escape
from chatbot import *

app = Flask(__name__)
bot = ChatBot()

@app.route("/ask/<question>")
def hello(question):
    ans = bot.ask(escape(question))
    return ans