for i in range(20):
    i += 1
    if i % 15==0:
        print('FizzBuzz')
    elif i % 5==0:
        print('Buzz')
    elif i % 3==0:
        print('Fizz')
    else:
        print(i)

msg = 'hello'
ls = list(msg)
print(ls)

word = input('英単語>>')
ls = list(word)
if len(word) == len(set(ls)):
     print('同じアルファベットは含まれていない')
else:
    print('同じアルファベットが含まれている')

