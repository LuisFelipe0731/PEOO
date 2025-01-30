sim = True
lista1 = []
while sim:
    dic = {}
    nome = input("Digite um nome: ")
    dic['nome'] = nome
    
    matri = (input("Digite uma matricula: "))
    dic['matricula'] = matri
    
    ano = matri[0:4]
    dic['ano de ingresso'] = ano
    
    lista1.append(dic)
    
    sim = input("Deseja continuar adicionando: ")
    
    
    
    if sim == 'n':
        sim = False
for y in lista1:
    print(y)