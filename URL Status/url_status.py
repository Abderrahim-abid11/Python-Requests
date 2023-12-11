import requests

try:
    light_green = "\033[1;32m"
    light_red = "\033[1;31m"
    light_blue = "\033[1;33m"

    url = str(input("Enter your url : "))
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        print(light_green, end="")
        print(f"[{url}] [{r.status_code}]")
    elif r.status_code == 302:
        print(light_blue, end="")
        print(f"[{url}] [{r.status_code}]")
    elif r.status_code == 404:
        print(light_red, end="")
        print(f"[{url}] [{r.status_code}]")
    else:
        print(f"[{url}] [{r.status_code}]")
except:
    print("Enter Valid URL!")
