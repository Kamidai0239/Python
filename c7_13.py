import requests
response=requests.get('https://www.python.org/downroads/')
text=response.text
print(text)
