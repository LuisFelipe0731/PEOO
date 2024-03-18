#Função: Ultimo dia do mês 
def Ultmes(mes,ano):
    if mes == 1 or mes == 3:
        print(f"31/0{mes}/{ano}")
    if mes == 5 or mes == 7:
        print(f"31/0{mes}/{ano}")
    if mes == 8 or mes == 10 or mes == 12:
        print(f"31/0{mes}/{ano}")
    if mes == 2:
        print(f"28/0{mes}/{ano}")
    else:
        print(f"30/0{mes}/{ano}")

Ultmes(8,2007)