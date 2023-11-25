import requests 

# GET = get - obtaining
# POST = post - create
# PUT = put - updating  
# DELETE = delete - deleting

url = "https://httpbin.org/delete"
response = requests.delete(url, params={'name':'Camel'}, headers={'version': '2.0'}, data={'id': 1})

if response.status_code == 200:
   print(response.text)