import requests

#http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file

post_url = "http://localhost:5000/"
fin = open('12-114-2.wav', 'rb')
get_url = "http://localhost:5000/uploads/" + '12-114-2.wav'
print(get_url)
files = {'file': fin}
try:
  r = requests.post(post_url, files=files)
  print (r.text)
  r = requests.get(get_url)
  print (r.text)
finally:
  fin.close()
