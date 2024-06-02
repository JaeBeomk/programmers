# 랜덤으로 7개의 숫자를 받자
# 중복은 안돼

import random
choice=[]
for i in range(7):
    i=random.randrange(1,46)
    if i not in choice:
        choice.append(i)


print("lotto번호는:{}".format(choice[:-1]),"\n",
      "+번호:{}".format(choice[-1]))

    