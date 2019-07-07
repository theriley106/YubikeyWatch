import os
import main
import json
from flask import Flask, request

app = Flask(__name__)

# Called whenever the app's callback URL receives a POST request
@app.route('/', methods=['POST'])
def webhook():
	# 'message' is an object that represents a single GroupMe message
	print(request.get_json())
	# Prints the payload to the console
	main.check_message(request.get_json())
	# Checks to see how to respond to the message
	return "ok", 200

if __name__ == '__main__':
	app.run('0.0.0.0', port=8000, debug=True)
