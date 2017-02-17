import requests
import time

from pprint import pprint

AI_DEBUG=False

def face_age(token, image_url):
    data = {'image_url' : image_url}
    return callEndpoint("https://aiception.com/api/v2.1/face_age", token, data)

def detect_object(token, image_url):
    data = {'image_url' : image_url}
    return callEndpoint("https://aiception.com/api/v2.1/detect_object", token, data, initial_wait=2000)

def adult_content(token, image_url):
    data = {'image_url' : image_url}
    return callEndpoint("https://aiception.com/api/v2.1/adult_content", token, data, initial_wait=2000)

def faces(token, image_url):
    data = {'image_url' : image_url}
    return callEndpoint("https://aiception.com/api/v2.1/face", token, data, initial_wait=2000)

def artistic_image(token, image_url, style_url):
    data = {
        'image_url' : image_url,
        'style_url' : style_url
    }
    return callEndpoint("https://aiception.com/api/v2.1/artistic_image", token, data, initial_wait= 50*1000, increment_wait= 15*1000, retries=30)


def callEndpoint(endpoint, token, datapayload, initial_wait=1000, increment_wait=1000, retries=20):

    r = requests.post(endpoint, auth=(token, 'password is ignored'), json=datapayload)

    if AI_DEBUG:
        print('Headers')
        pprint(r.headers)

        print('Server response to our POST request')
        pprint(r.json())

    task_url = r.headers['Location']

    # sleep initial_wait
    time.sleep(float(initial_wait)/1000)

    for _ in range(retries):
        r = requests.get(task_url, auth=(token, 'password is ignored'))
        if AI_DEBUG:
            pprint(r.json())
        if 'answer' in r.json():
            if isinstance(r.json()['answer'], str):
                if AI_DEBUG:
                    print("not done")
                pass
            else:
                if AI_DEBUG:
                    print("done")
                return r.json()
        # sleep increment_wait
        time.sleep(float(increment_wait) / 1000)
    return None