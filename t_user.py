import requests
import sys

sys.stdout = open('out.txt', 'w+')

resp = requests.get('https://twitter.com/users/username_available?username=whatever')
print(resp.text)


# from requests_html import HTMLSession

# session = HTMLSession()

# r = session.get('https://twitter.com/aiuawbfaksjbffuwqfn')

# r.html.render()  # this call executes the js in the page