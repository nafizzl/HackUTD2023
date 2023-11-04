from flask import Flask, redirect, url_for, request, jsonify, render_template
from google.cloud import dialogflow

stateBot = Flask(__name__)                              # create Flask instance

@stateBot.route('/', methods = ["GET", "POST"])
def bot():
    if request.method() == "POST":
        return redirect(url_for("chatBot.html"))            # if button is pressed, go to the chatbot
    else:
        return render_template("botHome.html")

@stateBot.route("/chatbot", methods = ["GET", "POST"])
def chatBot():
    if request.method() == "POST" and request.form.get("button") == "Send Message":
        userInput = request.json["userInput"]           # "userInput" is received from Vue.js

        # add code for processing the userInput request...
        botOutput = process(userInput)

        return jsonify({"botOutput" : botOutput})       # output "botOutput", bot's response
    
    elif request.method() == "POST" and request.form.get("button") == "Back to Home":
        return render_template("botHome.html")          # go back to home page
    
    else:
        return render_template("chatBot.html")          # display the chatbot window normally


if __name__ == "__main__":
    stateBot.run(debug=True)