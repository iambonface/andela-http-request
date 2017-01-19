""""
An API to fork my own github data with username iambonface

"""

import requests

req = requests.request('GET', 'http://api.github.com/users/iambonface')
print(req.json())

