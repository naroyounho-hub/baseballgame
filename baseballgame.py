# 야구 게임 3개의 숫자를 0~9 사이에서 고르고 맞추는 게임

import random

a = random.sample(range(1, 10), 3)
a2 = f"{str(a[0])+str(a[1])+str(a[2])})"
print(a2)
b = 0
a1 = print(input("숫자 : "))
s = 0
while s == 3:
    if a1 // 100 == a2 // 100:
        s += 1
    elif a1 // 100 in a:
        b += 1
        if (a1 % 100) // 10 == (a2 % 100) // 10:
            s += 1
        elif (a1 % 100) // 10 in a:
            b += 1
            if a1 % 10 == a2 % 10:
                s += 1
            elif a1 % 10 in a:
                b += 1
                print(f"(스트라이크 : {s} / 볼 : {b})")
