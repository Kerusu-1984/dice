import random
from re import match

if dice := match(r"^([0-9]+)[dD]([0-9]+)$",input("ダイス数dダイス面数　の形で入力してください　例 3d6  ")):
    n = int(dice.group(1))
    m = int(dice.group(2))
    dicelist = []

    for i in range(n):
        dicelist.append(random.randrange(1,m+1))
        
    print(dicelist)
    print("=> " + str(sum(dicelist)))


else:
    print("正しく入力してください")




