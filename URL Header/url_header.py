import requests

url = str(input("Enter your url : "))
r = requests.get(url, stream=True)

if (r.status_code == 200 or 302):
    for key, value in r.headers.items():
        print(f"{key} : {value}")
else:
    print(f"[{url}]  [{r.status_code}]")
