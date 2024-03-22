sim = True
dic = {'nome':' ' , 'matricula': ' ','ano de ingresso': ' '}
lista1 = []
while sim:
    nome = input("Digite um nome: ")
    dic['nome'] = nome
    
    matri = (input("Digite uma matricula: "))
    dic['matricula'] = matri
    
    sim = input("Deseja continuar adicionando: ")
    
    
    if sim == 'n':
        sim = False

print(dic)


