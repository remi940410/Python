#猜數字
import random 
n = random.randint(1,100) 
print(n)
num=0 
while (num != n):
    num = int(input("猜猜我設定的數字是多少?")) 
    if num > n:
        print("再小一點") 
    elif num< n: print("再大一點") 
    else: print("答對了!!")