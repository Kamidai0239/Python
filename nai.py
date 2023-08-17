import random
import pprint
"""
#内包表記
ls = [ i for i in range(1,11)]
print(ls) #[1,2,3....10]
ls = [ i**2 for i in range(1,11)]
print(ls) #[1,4,9....100]

#サイコロを3回振った時の目をリストにする
dices = [random.randint(1,6) for i in range(3)]
print(dices) #[4,2,6]

ls = [ str(i) for i in range(1,11)]
#print(ls) ['1','2','3',....'10']

#ls = [ for i in range(1,10) if i % 2 == 0]
print(ls) #[2,4,6,8]

"""
ls=[]
for i in range(1,10):
    if i % 2 ==0:
        ls.append(i)
"""
ls = [i*j for i in range(1,3) for j in range(1,3)]
print(ls) #[1,2,3,4]

"""
ls=[]
for i in range(1,3):
    for j in range(1,3):
            ls.append(i*j)
"""

ls = [[i] * 3 for i in range(3)]
print(ls) #[[0,0,0],[1,1,1],[2,2,2]]

"""
ls =[] 
for i in range(3):
    ls.append([i]*3)
"""

#ls = [[ for i in range(3)] for i in range(3)]
print(ls) #[[0,0,0],[0,1,2],[0,2,4]]


ls = [[i*j for j in range(1,10)]for i in range(1,10)]
pprint.pprint(ls)

#3,5

st1 = input()
ls1 = st1.split(' ')
ls1 = [int(i) for i in ls1]


n1,n2 = [ int(i) for i in input().split(' ')]
print(n1,n2)
"""

ls = sorted([random.randint(0,100) for i in range(100)],reverse=True)[:10]
print(ls)

