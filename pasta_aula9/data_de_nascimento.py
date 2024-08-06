import datetime
#Striptime e Fromisoformat

nasc = input("Informe sua data de nascimento(dd/mm/aaaa): ")

data = datetime.datetime.strptime(nasc, "%d/%m/%Y")

hoje = datetime.datetime.now()

print(data)
print((hoje - data)//30)