import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests
from StringIO import StringIO
import requests
import shutil
import json
import os

MY_BOT_ID = "ba10a3a35929f5dd3355adfe46"
MY_ACCESS_TOKEN = "6cShuodySHWkzDi1ION0f4cnQAZAH1GeofRkbmqW"
DEFAULT_PIC = "https://placeimg.com/512/512/tech"

def is_yubikey(stringVal):
	return bool(re.match("^(c{6}\w{38})+$", stringVal))

def download_image(url):
	# This downloads the profile picture from GroupMe
	if url == None:
		url = DEFAULT_PIC
	response = requests.get(url)
	return Image.open(StringIO(response.content))

def pretend_to_save_to_file(img):
	# Takes in an Image object
	# Returns an opened "File"
	output = StringIO()
	img.save(output, "PNG")
	data = output.getvalue()
	output.close()
	return data

def upload_an_image_to_group_me(img):
	# Takes in a Image object
	# Returns a string containing a groupme image url
	data = pretend_to_save_to_file(img)
	headers = {
	    'X-Access-Token': MY_ACCESS_TOKEN,
	    'Content-Type': 'image/jpeg',
	}
	response = requests.post('https://image.groupme.com/pictures', headers=headers, data=data)
	print response.text
	return response.json()['payload']['picture_url']


def post_image_to_group_me(img):
	# Takes in an Image object
	# Returns nothing
	data = {"bot_id"  : MY_BOT_ID,
	  "text"    : "sToP PoStInG YoUr yUbIkEy iN ThE GrOuP Me",
	  "attachments" : [
	    {
	      "type"  : "image",
	      "url"   : upload_an_image_to_group_me(img)
	    }
	  ]
	}
	response = requests.post('https://api.groupme.com/v3/bots/post', json=data)



def create_image(callBack):
	# This function creates the meme image
	# Takes in the data sent as a post request from GroupMe
	img = Image.open("image.png")
	# Opens up the meme template
	font = ImageFont.truetype("arial.ttf", 22)
	# Sets the font size and font type for the top of the meme
	old_size = img.size
	# This is the original size of the meme image
	new_im = Image.new("RGB", (300, 200), (255, 255, 255))   ## luckily, this is already black!
	# Creates a new image with a blank border
	draw = ImageDraw.Draw(new_im)
	# Sets up the picture to add the text to it
	draw.text((8, 38),"{}: ".format(callBack['name'].split(" ")[0]),(0,0,0),font=font)
	# Writes the persons name on top of the meme
	new_im = new_im.resize((1200, 800))
	# Resizes the text to make that blurry look
	new_im.paste(img, ((0, 0)))
	#new_im.show()
	profile = download_image(callBack.get("avatar_url")).resize((900,500))
	# Downloads and resizes the image for the meme
	font = ImageFont.truetype("arial.ttf", 40)
	# Sets the font size and font type for the bottom of the meme
	draw = ImageDraw.Draw(profile)
	# Sets up the picture to add the text to it
	draw.text((20, 440),'"' + callBack['text'] + '"',(255,255,0),font=font)
	# Adds the yubikey to the top of the meme before the profile picture
	new_im.paste(profile, ((30, 270)))
	# Pastes the profile picture on top of the meme
	#new_im.save('sample-out.png')
	# ^ This saves the profile picture
	post_image_to_group_me(new_im)
	# Posts the image to the GroupMe

def check_message(callBack):
	if is_yubikey(callBack["text"]):
		create_image(callBack)

if __name__ == '__main__':
	#download_image("https://i.groupme.com/512x512.jpeg.a434c84db02b44098180cf9b79530cf0", 'myImage.jpeg')
	print is_yubikey("ccccccjeijnguibcufrkkdhlnfuicgbrnvrbbijevbbe")
	create_image(callBack)
