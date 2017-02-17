import shutil
from aiception import *


token = "YOUR_TOKEN_HERE"
image_url = "https://upload.wikimedia.org/wikipedia/commons/0/06/Morgan_Freeman,_2006_(cropped).jpg"
style_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1280px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"

# call AIception API (takes around 55 seconds)
r = artistic_image(token, image_url, style_url)
print(r)

# select the image at iteration '300'
image_url = [elem['image_url'] for elem in r['answer']['urls'] if elem['iteration'] == '300'][0]

# download the image
file_name = "my_image.png"
response = requests.get(image_url, stream=True)
with open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
