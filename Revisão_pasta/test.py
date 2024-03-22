si = []
sim = True

while sim:
    num = int(input())
    si.append(num)

    sim = input("Deseja continuar? ")

    if sim == 'n':
        sim = False

print(si)
