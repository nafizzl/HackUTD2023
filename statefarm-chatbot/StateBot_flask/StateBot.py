from flask import Flask, redirect, url_for, request, jsonify, render_template 
from google.cloud import dialogflow_v2
from google.api_core.exceptions import InvalidArgument

stateBot = Flask(__name__)                              # create Flask instance
dialogFlowClient = dialogflow_v2.SessionsClient()       # create DialogFlow session client

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
        jake = dialogFlowClient.session_path('project-id', 'sess-id')          # assign session via client
        # replace project-id and sess-id with actuall project and uniq sess sid
        usrTxt = dialogflow_v2.TextInput(text=userInput, language_code='en-US')
        que = dialogflow_v2.QueryInput(text=usrTxt)                            # input message with US English and send to query

        try:    
            jakeTalk = dialogFlowClient.detect_intent(session=jake, query_input=que)    # get the input and process to output something else

            jakeTruth = jakeTalk.query_result.fulfillment_text      # get the output of the query

            return jsonify({"botOutput" : jakeTruth})       # output "botOutput", bot's response

        except InvalidArgument as err:
            return jsonify({"botOutput" : "Error:" + str(err)})     # output 

    elif request.method() == "POST" and request.form.get("button") == "Back to Home":
        return render_template("botHome.html")          # go back to home page
    
    else:
        return render_template("chatBot.html")          # display the chatbot window normally


if __name__ == "__main__":
    stateBot.run(debug=True)