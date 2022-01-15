from payment import payment
from cardsforht    import card
import time
import random




coll=0


def primeGreaterThan2(num):
    while True:
        if num % 2 == 1:
            isPrime = True
            for x in range(3, int(num ** 0.5), 2):
                if num % x == 0:
                    isPrime = False
                    break
            if isPrime:
                return num
        num = num + 1
    return num


def djb2(arr):
    hash = 5381
    for x in arr:
        hash = (( hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF

 
def hash(arr):
    return djb2(arr)%N


def collisions(item, check=False):
    global coll
    new_slot=hash(item.name)
    counter=0
    while hash_table[new_slot]!=None and hash_table[new_slot].name!=item.name :
        counter+=1
        new_slot = (hash(item.name) + counter*counter) % N
    
    if hash_table[new_slot]==None:
        hash_table[new_slot]=card(item)
        if check:
            coll+=1
    else:
        hash_table[new_slot].addData(item.amount,item.day)






def rehash():
    global hash_table,N
    New_N=primeGreaterThan2(2*N)
    old_hash=hash_table.copy()
    hash_table=[None]*New_N
    for item in old_hash:
        if item==None:
            continue
        keys=hash(item.name)
        if hash_table[keys]!=None:
            collisions(pay)
            continue
     
    hash_table[key]=item




    






print("calculating time...")
t0=time.time()
N=10000
load_factor=0.6
items=1000000
hash_table=[None]*N
coll=0
for i in range(items):
    pay=payment()
    key=hash(pay.name)
    if(i/N)>load_factor:
        rehash()
        continue
    if hash_table[key]!=None:
        collisions(pay,check=True)
        continue
    hash_table[key]=card(pay)



dt=time.time()-t0
print('Time taken to generate Hash table:',dt,'seconds')