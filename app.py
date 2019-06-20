
# RESOURCE: http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/


# IMPORTS
import os
import main
import json
from flask import Flask, request

app = Flask(__name__)

# Called whenever the app's callback URL receives a POST request
@app.route('/', methods=['POST'])
def webhook():
	# 'message' is an object that represents a single GroupMe message.
	print(request.get_json())
	main.check_message(request.get_json())
	return "ok", 200

if __name__ == '__main__':
	app.run('0.0.0.0', port=8000, debug=True)
