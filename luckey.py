import random
luckey = 7777
count = 0
while True:
    count += 1
    n=random.randint(1,9999)
    print(f'count: {n}')
    if n == luckey:
        break
print(f'{count}回目に7777が出ました！')
