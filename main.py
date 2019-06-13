import re
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

def is_yubikey(stringVal):
	return bool(re.match("^(c{6}\w{38})+$", stringVal))

callBack = {
  "attachments": [],
  "avatar_url": "https://i.groupme.com/123456789",
  "created_at": 1302623328,
  "group_id": "1234567890",
  "id": "1234567890",
  "name": "Akul",
  "sender_id": "12345",
  "sender_type": "user",
  "source_guid": "GUID",
  "system": False,
  "text": "ccccccjeijnguibcufrkkdhlnfuicgbrnvrbbijevbbe",
  "user_id": "1234567890"
}

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

	draw.text((8, 38),"{}: ".format(callBack['name']),(0,0,0),font=font)
	new_im = new_im.resize((1200, 800))

	new_im.paste(img, ((0, 0)))
	#new_im.show()
	profile = Image.open("0.png")
	profile = profile.resize((900,500))
	font = ImageFont.truetype("arial.ttf", 40)
	# draw.text((x, y),"Sample Text",(r,g,b))

	draw = ImageDraw.Draw(profile)

	draw.text((20, 440),'"' + callBack['text'] + '"',(255,255,0),font=font)
	new_im.paste(profile, ((30, 270)))
	new_im.save('sample-out.png')
	pass

def check_message(callBack):
	if is_yubikey(callBack["text"]):
		create_image()

if __name__ == '__main__':
	print is_yubikey("ccccccjeijnguibcufrkkdhlnfuicgbrnvrbbijevbbe")
	create_image(callBack)