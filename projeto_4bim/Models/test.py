from livro import *
from genero import *
from exemplar import *
from compra import *

x = Livro(1, "O pequeno principe"," Antoine de Saint-Exupéry",'01/04/1943')
y = Livro(2,"Dracula","Bram Stoker",'26/05/1897')

a = Genero(3,"Terror","Genero que envolve medo e suspense")


Livros.inserir(x)
Livros.inserir(y)
Livros.salvar()
print(Livros.listar())
  


