# 利用 for 寫一個迴圈，讓使用者輸入要得到的平方最大值數。 例如輸入 7
# 顯示一行 1, 4, 9, 16, 25, 36

a=int(input("請輸入一個正整數:")) 
listAA=[] 
for i in range(1,a):
    listAA.append(i**2) 
print(listAA)