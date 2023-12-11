import requests
from fake_useragent import UserAgent
try:
    light_white = "\033[1;37m"
    url = str(input("Enter Image Url : "))
    type = str(input("Enter Image Type (jpg,png...) : "))
    ua = UserAgent()
    user_agent = ua.random
    headers = {
            "User-Agent" : user_agent,
            "Accept": f"image/{type}"
        }
    r = requests.get(url, headers=headers)
    with open("install_image.jpg", "wb") as f:
        f.write(r.content)
        print(light_white, end="")
        print("Image Download ...")
except:
    print("INVALID URL OR ERROR CONNECTION !")

