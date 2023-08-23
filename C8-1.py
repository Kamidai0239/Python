import urllib.request

url= 'https://blog.python.org/'
req= urllib.request.Request(url)

with urllib.request.urlopen(req) as res:
    body = str(res.read())

if 'sequrity' in body or 'vulnerability' in body:
    print('セキュリティに関する記述があります')
    print('http://blog.python.orgを確認してください')
else:
    print('調査対象のセキュリティ用語はありませんでした')

