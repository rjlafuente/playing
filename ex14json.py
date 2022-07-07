import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_1582996.json'

data = urllib.request.urlopen(url, context=ctx).read()

print('Retrieved', len(data), 'characters')
info = json.loads(data)

n = 0
for item in info['comments'] :
    n = n + float(item['count'])

print('The total is',n)
