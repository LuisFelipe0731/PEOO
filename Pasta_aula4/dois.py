num = []

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a%2 == 0:
    num.append(a)
if b%2 == 0:
    num.append(b)
if c%2 == 0:
    num.append(c)
if d%2 == 0:
    num.append(d)

print(num)