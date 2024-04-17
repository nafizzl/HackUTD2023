# HackUTD 2023: Statefarm ChatBot

https://devpost.com/software/jakebot

HackUTD's State Farm Design Challenge: Second Place Winner

Inspiration
Small businesses are often volatile and require quick response and intervention when something goes away from normal. A broken window, or malfunctioning machinery can be devastating to a small business. We were inspired by conversational models such as GPT and Claude, and tools that take advantage of a multitude of inputs such as documents and photos.

What it does
JakeBot is more than a Chat bot. It is an AI insurance assistant that can offer guidance, intervention, and results on any part of the insurance process in a quick manner. It offers natural, human like conversation thanks to Vertex.ai, and services including insurance quotes, claims filing and AI automated approval.

How we built it
We used Google Cloud's Dialogflow CX to create a virtual assistance agent, and embedded Vertex.AI to generate all responses in a humanlike manner. The kommunicate API was used for webpage integration and for the UI. A highlight of our project was the addition of AI document processing. We gave the example of a user submitting a police report of property damage, so that JakeBot can automatically verify its authenticity and payout for the claim on the spot. We used GitHub's Actions feature to deploy versions to Firebase Hosting. This allowed us to push out final products to our live production build in a matter of minutes. We envision JakeBot to serve as an expandable platform, integrating functionalities such as AI damage detection from photo, NLP report generation, AI generated image detection, and more. State Farm can use AI to automate as many tasks as possible, and JakeBot is the perfect platform to build upon.

Challenges we ran into
API's, especially Flask, and Google Cloud functions.

Accomplishments that we're proud of
Having a final product!

What we learned
Experience with Google Cloud, and development in an extremely fast paced environment.

What's next for JakeBot
Serve as an ever-expandable platform for State Farm to create a true AI assistant that actually saves them time and resources.
