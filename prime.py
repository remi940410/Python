# 質數問題 
def isPrime(n):
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True

num = int(input("輸入要判斷的質數的數字:")) 
if isPrime(num) == True:
    print("Yes")
else:
    print("No")
