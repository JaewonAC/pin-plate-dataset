from pathlib import Path
import random
import requests
import json

files = {}
count = 0

for filename in random.sample(list(Path('.').glob('*.jpg')), 3):
    print(filename)
    with open(filename, 'rb') as data:
        files.update(
            {('client_files[' + str(count) + ']'):
                 (filename.name,
                  data.read(),
                  'image/jpeg')})
        count += 1

data = {}
data.update({'image_quality':70})
data.update({'use_zip_chunks':True})

req = requests.Request('post',
                       'http://localhost:8080/api/v1/task/22/data',
                       data=data,
                       files=json.dumps(files)).prepare()
