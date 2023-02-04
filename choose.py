# 先詢問客人吃飯或麵 #選了飯之後再詢問
# 要排骨飯還是雞腿飯
# 最後顯示 你選吃飯，以及所點的飯類 # 選了麵之後再詢問
# 要牛肉麵還是米粉湯
# 最後顯示 你選吃麵，以及所點的麵類
text1 = input("請輸入吃麵或吃飯") 
if (text1 == "吃飯"): 
    text2 = input("要排骨飯還是雞腿飯")
    if (text2 == "排骨飯"):
        print("排骨飯") 
    else:
        print("雞腿飯")
    print("你選吃飯",text2) 
else:
    text3 = input("要牛肉麵還是米粉湯")
    if(text3 == "牛肉麵"): 
        print("牛肉麵") 
    else: 
        print("米粉湯")
    print("你選吃麵",text3)