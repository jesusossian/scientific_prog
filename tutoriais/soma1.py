############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
##############################################################################

import sys
sys.path.insert(0,'/home/jossian/repository/scientific_prog')
import entrada1

lista = []
for x in range(10):
    lista.append(entrada1.valida_inteiro("Digite um número:", 0, 20))
print(f"Soma: {sum(lista)}")
