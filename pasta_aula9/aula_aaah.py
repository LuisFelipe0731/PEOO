import datetime
#aula - datas

aula_de_gilbert = datetime.datetime(2024, 8, 6, 14, 30)

c = datetime.datetime.now()#Mostra a data de hoje
s = c.strftime("%A, %d/%B/%Y")
print(aula_de_gilbert)
print(c)
print(s)