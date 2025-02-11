from livro import *

x = Livro(1, "O pequeno Principe"," Antoine de Saint-Exupéry",'01/04/1943')
y = Livro(2,"Dracula","Bram Stoker",'26/05/1897')

Livros.inserir(x)
Livros.inserir(y)

for l in Livros.listar():
    print(l)
