from aiception import *
from pprint import pprint

token = "YOUR_TOKEN_HERE"
image_url = "https://upload.wikimedia.org/wikipedia/commons/0/06/Morgan_Freeman,_2006_(cropped).jpg"

# call AIception API
r = face_age(token, image_url)
pprint(r)
