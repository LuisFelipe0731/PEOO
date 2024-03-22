s = []
sim = True

while sim:
    num = int(input())
    s.append(num)

    sim = input("Deseja continuar? ")

    if sim == 'n':
        sim = False

print(s)
