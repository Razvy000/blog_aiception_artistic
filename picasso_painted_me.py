from aiception import *

token = "YOUR_TOKEN_HERE"
image_url = "https://upload.wikimedia.org/wikipedia/commons/0/06/Morgan_Freeman,_2006_(cropped).jpg"
style_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1280px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"

#r = face_age(token, image_url)
#print(r)
#print(r['answer']['age'])

# r = detect_object(token, image_url)
# print(r)

# r = adult_content(token, image_url)
# print(r)

# r = faces(token, image_url)
# print(r)

r = artistic_image(token, image_url, style_url)
print(r)

# r = {'answer': {'urls': [{'image_url': 'https://s3.eu-central-1.amazonaws.com/aiception.com/2017/02/task-111-JAViGPaTEIjl7nqbiPDBixoK5WMUCVfEU4yepIOzhQZ3mcqFRAVbuaJFiv0c.png',
#                       'iteration': '100'},
#                      {'image_url': 'https://s3.eu-central-1.amazonaws.com/aiception.com/2017/02/task-111-bMTszCCDQGNEyf806FKE6fx7lhcZjKGdSNCjNkZFrAGDMFfvtq3in6FMolo0.png',
#                       'iteration': '300'},
#                      {'image_url': 'https://s3.eu-central-1.amazonaws.com/aiception.com/2017/02/task-111-VPIAdy2Njoa8gOo6pOnmtBJMrReSSVIfrCmjYph5rfQbdsXXMQlCE2Gm6ho1.png',
#                       'iteration': '200'}]},
#  'created_at': 'Fri, 17 Feb 2017 15:33:44 GMT',
#  'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Taylor_Swift_GMA_2012.jpg/870px-Taylor_Swift_GMA_2012.jpg',
#  'state': 'done',
#  'style_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1280px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg',
#  'this_url': 'https://aiception.com/api/v2.1/artistic_image/111',
#  'type': 'artistic_image'}

print(r['answer'])
image_url = [elem['image_url'] for elem in r['answer']['urls'] if elem['iteration'] == '300'][0]
print(image_url)

#file_name = image_url.rsplit('/', 1)[-1]
file_name = "my_image.png"

import shutil
response = requests.get(image_url, stream=True)
with open(file_name, 'wb') as out_file:
     shutil.copyfileobj(response.raw, out_file)
