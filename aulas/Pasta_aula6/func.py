r = input().split()

t = list(map(int,r))
num = 0
for x in t:
    if x%2 == 0:
        num +=1

print(num)