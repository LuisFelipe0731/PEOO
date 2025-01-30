import enum

#Aula sobre inumeração 13/08/2024

class Estacao(enum.Enum): #Enum: Apenas um valor
    outono = 1
    inverno = 2
    primavera = 3
    verao = 4

class Dia(enum.IntFlag):
    domingo = 1
    segunda = 2
    terca = 4
    quarta = 8
    quinta = 16
    sexta = 32
    sabado = 64


c = Estacao(4)
d = Dia(2) | Dia(8)
print(c)
print(d)