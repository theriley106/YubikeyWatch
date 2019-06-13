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

def is_yubikey(stringVal):
	return bool(re.match("^(c{6}\w{38})+$", stringVal))

callBack = {
    "attachments": [],
    "source_guid": "86399e2d08967d6b98c10d91891f0a93",
    "text": "I'm sorry that I keep doing this",
    "sender_id": "38003981",
    "system": False,
    "id": "156038905715356108",
    "user_id": "38003981",
    "name": "Christopher Lambert",
    "created_at": 1560389057,
    "sender_type": "user",
    "avatar_url": "https://i.groupme.com/512x512.jpeg.a434c84db02b44098180cf9b79530cf0",
    "group_id": "47732680"
}

def download_image(url, saveAs):
	response = requests.get(url)
	img = Image.open(StringIO(response.content))
	img = img.resize((1200, 800))
	img.save("testing.jpeg")

def create_image(callBack):
	img = Image.open("image.png")
	#draw = ImageDraw.Draw(img)
	# font = ImageFont.truetype(<font-file>, <font-size>)
	font = ImageFont.truetype("arial.ttf", 22)
	# draw.text((x, y),"Sample Text",(r,g,b))
	old_size = img.size

	new_size = (300, 200)
	new_im = Image.new("RGB", new_size, (255, 255, 255))   ## luckily, this is already black!


	draw = ImageDraw.Draw(new_im)

	draw.text((8, 38),"{}: ".format(callBack['name'].split(" ")[0]),(0,0,0),font=font)
	new_im = new_im.resize((1200, 800))

	new_im.paste(img, ((0, 0)))
	#new_im.show()
	response = requests.get(callBack.get("avatar_url"))
	profile = Image.open(StringIO(response.content))
	profile = profile.resize((900,500))
	font = ImageFont.truetype("arial.ttf", 40)
	# draw.text((x, y),"Sample Text",(r,g,b))

	draw = ImageDraw.Draw(profile)

	draw.text((20, 440),'"' + callBack['text'] + '"',(255,255,0),font=font)
	new_im.paste(profile, ((30, 270)))
	new_im.save('sample-out.png')

	output = StringIO()
	format = 'PNG' # or 'JPEG' or whatever you want
	new_im.save(output, format)
	data = output.getvalue()
	output.close()


	headers = {
	    'X-Access-Token': 'jZCDAeFXqOxmo3IFB6bhmcqnDj5d5WZ90sobykeG',
	    'Content-Type': 'image/jpeg',
	}
	response = requests.post('https://image.groupme.com/pictures', headers=headers, data=data)
	#os.system("curl 'https://image.groupme.com/pictures'" + ' -X POST -H "X-Access-Token: jZCDAeFXqOxmo3IFB6bhmcqnDj5d5WZ90sobykeG" -H "Content-Type: image/jpeg" --data-binary @sample-out.png > t.txt')

	a = json.load(open('t.txt'))
	print a
	a = a['payload']['picture_url']
	x = '''{"bot_id"  : "14b11096b7b9e36470dfc5e083","text"    : "Hello world","attachments" : [{"type"  : "image","url"   : "''' + a + '''"}]}'''
	os.system('''curl -d '{}' https://api.groupme.com/v3/bots/post'''.format(x))

def check_message(callBack):
	if is_yubikey(callBack["text"]):
		create_image(callBack)

if __name__ == '__main__':
	#download_image("https://i.groupme.com/512x512.jpeg.a434c84db02b44098180cf9b79530cf0", 'myImage.jpeg')
	print is_yubikey("ccccccjeijnguibcufrkkdhlnfuicgbrnvrbbijevbbe")
	create_image(callBack)
