# import 시 주의할 점...
# import는 항상 최상단에 작성한다.
import random

menu = ['짜장면', '짬뽕', '탕수육']
# menu중에 하나를 무작위로 선택
# f(x)
choice = random.choice(menu)

print(choice)