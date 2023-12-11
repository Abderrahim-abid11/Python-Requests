import requests

try:
    light_yello = "\033[1;33m"
    url = str(input("Enter your url : "))
    r = requests.get(url, stream=True)
    print()
    if (r.status_code == 200):
        for value in r.headers:
            print(light_yello, end="")
            print(f"{value}")
    else:
        print()
        print(f"[{url}] [{r.status_code}]")
    print()
except:
    print("Envalid URL!")
