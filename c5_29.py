def eat(breakfast,lunch,dinner='カレー'):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'夜は{dinner}を食べました')

    for d in desserts:
        print(f'おやつに{d}を食べました')
    
print('8月1日')
eat('トースト','パスタ','カレー','アイス','チョコ','カレー')

def sumof(n1,*args):
    total=0
    for i in args:
        total+= i
    return total
    int(sumof()) #0
    print(sumof(3,5)) #8
    print(sumof(3,5,7)) #15
