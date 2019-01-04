# proprietary to BEERA // DO NOT COPY




import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
payload = {'txtU': '11610529', 'Txtpw': 'sreerAm31@(&)'}
url = 'http://ums.lpu.in'
r=requests.post(url, data=payload, verify=False)

print(r.url)
