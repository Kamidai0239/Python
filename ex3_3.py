isError = False
n = 50
if isError == False and n < 100:
    print('ok')

num = int(input('数値>>'))
if num % 2 == 0:
    print('偶数')
else:
    print('奇数')
    aisatu = input('挨拶'>>)

    if aisatu == 'こんにちは':
        print('ようこそ!')
    elif aisatu == '景気は?':
        print('ぼちぼちです')
    elif aisatu == 'さようなら':
        print('お元気で!')
    else:
        print('どうしました')

