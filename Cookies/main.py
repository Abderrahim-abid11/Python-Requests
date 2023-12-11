import requests

s = requests.session()
login_url = 'http://127.0.0.1:5000/login'
login_data = {'username': 'test', 'password': 'test'}

r = s.post(login_url, json=login_data)
cookie = r.cookies

if r.json().get('success'):
    print('login success.')
else:
    print('login faild!')
    
pro_url = 'http://127.0.0.1:5000/protected'
r = s.get(pro_url, cookies=cookie)

if r.json().get('access'):
    print('access success !')
else:
    print('access denied !')
