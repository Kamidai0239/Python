def eat(breakfast,lunch,dinner='カレー'):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'夜は{dinner}を食べました')
    
print('8月1日')
eat(breakfast='納豆ご飯'dinner='カレーうどん')
print('8月2日')
eat(dinner='カレーうどん',breakfast='納豆ご飯')
print('8月3日')
eat('納豆ご飯',dinner='カレーうどん')
