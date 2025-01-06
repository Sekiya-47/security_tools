"""
pip install ..

"""

import requests

# URLとパラメータ
url = 'https://example.com/api'
params = {'key': 'value'}

# GETリクエストの送信
response = requests.get(url, params=params)

# レスポンスの表示
print(response.text)
