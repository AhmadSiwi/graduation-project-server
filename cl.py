import requests

#http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file

file_name = '12-1-2.wav' # choose what ever file you want to be predicted
post_url = "http://localhost:5000/"
fin = open(file_name, 'rb')
get_url = "http://localhost:5000/uploads/" + file_name
#print(get_url)
files = {'file': fin}
try:
  r = requests.post(post_url, files=files)
  #print (r.text)
  r = requests.get(get_url)
  print (r.text)
finally:
  fin.close()
