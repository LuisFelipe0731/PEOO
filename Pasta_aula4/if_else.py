bas = input().split()
a = float(bas[0])
b = float(bas[1])
c = float(bas[2])
if a or b or c <= 0:
    print("Impossivel calcular")
    
delta = (b**2) - (4*a*c)


r1 = ((-b) + (delta**0.5))/(2*a)
r2 = ((-b) - (delta**0.5))/(2*a)
print(f"R1 = {r1:.5f}")
print(f"R2 = {r2:.5f}")