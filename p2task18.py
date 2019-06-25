age = int(input())
if age % 2 == 0:
    for i in range(0, age+1):
        if i % 2 == 0:
            print(i)
elif age % 2 != 0:
    for k in range(0, age+1):
        if k % 2 != 0:
            print(k)
