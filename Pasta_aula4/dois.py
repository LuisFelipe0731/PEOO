num = input().split()

a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])

for x in num:
    div = x % 2
    if div == 0:
        print(x)