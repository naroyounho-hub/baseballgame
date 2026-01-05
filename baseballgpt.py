import random

a = random.sample(range(1, 10), 3)
a2 = f"{a[0]}{a[1]}{a[2]}"
print(a2)  # 테스트용 (정답)

while True:
    b = 0
    s = 0

    a1 = int(input("숫자 : "))

    # 100의 자리
    if a1 // 100 == int(a2) // 100:
        s += 1
    elif a1 // 100 in a:
        b += 1

    # 10의 자리
    if (a1 % 100) // 10 == (int(a2) % 100) // 10:
        s += 1
    elif (a1 % 100) // 10 in a:
        b += 1

    # 1의 자리
    if a1 % 10 == int(a2) % 10:
        s += 1
    elif a1 % 10 in a:
        b += 1

    print(f"(스트라이크 : {s} / 볼 : {b})")

    if s == 3:
        print("정답")
        break
