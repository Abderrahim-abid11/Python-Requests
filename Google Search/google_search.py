import requests

API_KEY = 'AIzaSyCAvf0ONQckLyTz_yjI9GAK6mzZIbpT00k'
SEARCH_ENGINE_ID = '051285004281a474a'

query = str(input("What Are You Searching For : "))
#type = str(input("Enter Search Type : "))
#file = str(input("Enter File Type : "))
url = 'https://www.googleapis.com/customsearch/v1'
params = {
        'q': query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        #'searchType' : f"{type}",
        #'fileType' : f"{file}"
        }

r = requests.get(url, params=params)
results = r.json()['items']


for i in results:
   print(i['link'])
