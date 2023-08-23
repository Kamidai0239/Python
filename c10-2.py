try:
    price = int(input('料金を入力>>'))
    number = int(input('人数を入力>>'))
    print(f'1人あたり{price/number}円です')
    print('料金または人数は整数を入力してください')
except :
    print('人数には0を入力しないでください')

print('プログラムを終了します')

