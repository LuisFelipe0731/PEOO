frase = input()
total = 0
for x in frase:
    if "0" <= x <= "9":
        total = total + int(x)
        
print(total)