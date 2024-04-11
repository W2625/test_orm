import requests
url = 'https://m.ip138.com/iplookup.php?ip='
try:
    r = requests.get(url + '157.46.8.64' +'&action=2')
    print(r.request.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')
'''
r = requests.get('https://m.ip138.com/iplookup.php?ip=' + '157.46.8.64' +'&action=2')
print(r.request.headers)
'''