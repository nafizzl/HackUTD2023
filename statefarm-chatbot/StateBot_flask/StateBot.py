from flask import Flask, redirect, url_for, request, jsonify, render_template, session 
from google.cloud import dialogflowcx_v3
from google.api_core.exceptions import InvalidArgument
import os
import uuid
import requests

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\19295\HackUTD2023\statefarm-chatbot\StateBot_flask\hackutd-statefarmbot-040f14ef256e.json"

stateBot = Flask(__name__)                              # create Flask instance
dialogFlowClient = dialogflowcx_v3.SessionsClient()       # create DialogFlow session client

@stateBot.route('/', methods = ["GET", "POST"])
def bot():
    if request.method == "POST" and request.form.get("Ask Jake") == "Ask Jake":
        return redirect(url_for("chatBot"))            # if button is pressed, go to the chatbot
    else:
        return render_template("botHome.html")

@stateBot.route("/chatbot", methods = ["GET", "POST"])
def chatBot():
    if request.method == "POST" and request.form.get("sendButton") == "Send Message":
        #userInput = request.json.get("userInput")          # "userInput" is received from Vue.js
        userInput = request.form.get("userInput")
        print("User input:", userInput)
        # add code for processing the userInput request...
        project_id = "hackutd-statefarmbot"
        location_id = "us-central1"
        agent_id = "da05e51c-445d-454c-b723-50b9171e77b1"
        sess_id = str(uuid.uuid4())
        jake = dialogFlowClient.session_path("hackutd-statefarmbot", "us-central1", "da05e51c-445d-454c-b723-50b9171e77b1", sess_id)          # assign session via client
        print(f"proj: {project_id}")
        print(f"loc: {location_id}")
        print(f"agent: {agent_id}")
        print(f"sesh: {sess_id}")

        usrTxt = dialogflowcx_v3.TextInput(text=userInput)
        que = dialogflowcx_v3.QueryInput(text=usrTxt, language_code="en-US")    # input message with US English and send to query

            
        jakeReq = dialogflowcx_v3.DetectIntentRequest(session=jake, query_input=que)
        
        try:
            print("Before intent")
            jakeTalk = dialogFlowClient.detect_intent(request=jakeReq)    # get the input and process to output something else
            print("After intent")
            jakeTruth = jakeTalk.query_result.fulfillment_text      # get the output of the query

            #return jsonify({"botOutput" : jakeTruth})       # output "botOutput", bot's response
            return jakeTruth
        except InvalidArgument as err:
            #return jsonify({"botOutput" : "Error: " + str(err)})     # output 
            return "Error"
        
    if request.method == "POST" and request.form.get("homeButton") == "Back to Home":
        return redirect(url_for("bot"))          # go back to home page
    
    else:
        return render_template("chatBot.html")          # display the chatbot window normally


if __name__ == "__main__":
    stateBot.run(debug=True)