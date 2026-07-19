import requests

url = 'http://localhost:8000/api/identify'
files = {'file': open('storage/uploads/sample.jpg','rb')}
r = requests.post(url, files=files)
print(r.json())
