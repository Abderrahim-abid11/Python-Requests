import requests
from fake_useragent import UserAgent

try:
    url = str(input("Enter Your Url : "))
    
    ua = UserAgent()
    user_agent = ua.random
    headers = {
        'User-Agent': user_agent,
    }

    r = requests.get(url, headers=headers)

    # Check if the request was successful 
    # (status code in the range 200-299)
    if 200 <= r.status_code < 300:
        body = r.text
        print()
        print(body)
    else:
        print(f"Error: Request failed with status code {r.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request Exception: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

