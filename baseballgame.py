# 야구 게임 3개의 숫자를 0~9 사이에서 고르고 맞추는 게임

import random

a = random.sample(range(1, 10), 3)
a2 = f"{a[0]}{a[1]}{a[2]}"
print(a2)
while True:
    a1 = int(input("숫자 : "))
    s = 0
    b = 0
    if a1 // 100 == int(a2) // 100:
        s += 1
    elif a1 // 100 in a:
        b += 1
    if (a1 % 100) // 10 == (int(a2) % 100) // 10:
        s += 1
    elif (a1 % 100) // 10 in a:
        b += 1
    if a1 % 10 == int(a2) % 10:
        s += 1
    elif a1 % 10 in a:
        b += 1
    print(f"(스트라이크 : {s} / 볼 : {b})")
    if s == 3:
        print("정답")
        break
