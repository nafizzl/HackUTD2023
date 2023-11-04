from flask import Flask

StateBot = Flask(__name__)

@StateBot.route('/')
def bot():
    return "I love State Farm!"

if __name__ == "__main__":
    StateBot.run(debug=True)