# # Calcule o módulo ( % ) de 17 por 4.


# # Multiplique 9 por 3 e, em seguida, eleve o resultado ao quadrado.
# # n = 9 * 3
# # n1 = n**2
# # print(n1)

# # # Calcule a raiz quadrada de 81.

# # # Adicione 20 a 3 vezes 4.
# # n = 20 + (3*4)
# # print(n)

# # # Multiplique 15 por 2 e, em seguida, subtraia 7.
# # n = (15 * 2) - 7
# # print(n)

# # # Eleve 5 ao cubo.
# # n = 5 ** 3
# # print(n)

# # # Calcule a média de 17, 21 e 25.

# # n = (17 + 21 + 25) / 3
# # print(n)

# # # Multiplique 11 por 2 e adicione 7.
# # n = (11 * 2) + 7
# # print(n)
# # # Subtraia 15 de 3 vezes 8 e divida o resultado por 2.
# # n = 15 - (3 * 8)
# # print(n)
# # n1 = n / 2
# # print(n1)

# # # Eleve 2 à potência de 10.

# # n = 2 ** 10
# # print(n)


# n = 1 
# num = [1, 2, 3]
# num[1] = 'teste'
# print(num)
# num.append(100)
# print(num)
# lista

# # ___________________________________________________________________________________


# produtos = ['','uva','pera','maçã','banana']
# valores = [0,10.50,5.0,15.25,10.0]
# carrinho = []
# total = []

# produ0 = int(input(f''' 
#                        escolha um a partir do indice:  
# {produtos[1]} - {produtos.index(produtos[1])} - R$ {valores[1]}
# {produtos[2]} - {produtos.index(produtos[2])} - R$ {valores[2]}
# {produtos[3]} - {produtos.index(produtos[3])} - R$ {valores[3]}
# {produtos[4]} - {produtos.index(produtos[4])} - R$ {valores[4]}



# '''))

# carrinho.append(produtos[produ0])
# total.append(valores[produ0])
# produ1 = int(input(f''' 
#                        escolha um a partir do indice:  
# {produtos[1]} - {produtos.index(produtos[1])} - R$ {valores[1]}
# {produtos[2]} - {produtos.index(produtos[2])} - R$ {valores[2]}
# {produtos[3]} - {produtos.index(produtos[3])} - R$ {valores[3]}
# {produtos[4]} - {produtos.index(produtos[4])} - R$ {valores[4]}



# '''))
# carrinho.append(produtos[produ1])
# total.append(valores[produ1])
# produ2 = int(input(f''' 
#                        escolha um a partir do indice:  
# {produtos[1]} - {produtos.index(produtos[1])} - R$ {valores[1]}
# {produtos[2]} - {produtos.index(produtos[2])} - R$ {valores[2]}
# {produtos[3]} - {produtos.index(produtos[3])} - R$ {valores[3]}
# {produtos[4]} - {produtos.index(produtos[4])} - R$ {valores[4]}


# '''))
# carrinho.append(produtos[produ2])
# total.append(valores[produ2])


# print('Carrinho', carrinho)

# print('R$', sum(total))

#_________________________________________________________________________________________________________________




# var  =  10
# lista  = [1,2,3]


# # inserir dados
# lista[1] = [1,0,0,5] # 1 dad0 ou lista
# lista.append(10) # inserir no final da lista, um valor ou lista
# lista.insert(0,150) # inserir no indice indicado
# lista.extend([1,2,3,5,5,6,4,5,5]) # inserir varios dados de uma vez  ou lista
# lista += (1,5,6,6,98,6)# inserir varios dados de uma vez  ou lista



# # deletar dados
# lista.remove(150) # remove a partir do dado que vc vê 
# lista.pop() # remove o último valor
# lista.pop(0) # remove o valor que esta posicionado no indice declado
# del lista[0] #deletando a partir do indice
# # slice -  fatiar 
# del lista[0:7]
# #    start : stop 
# lista_2 =  lista[0:7]



# # verifica 
# print(len(lista))# tamanho
# print(min(lista))# menor
# print(max(lista))# maior
# # lista.sort(reverse=True)
# lista.reverse()
# print(lista)




# lista3 = list(range(1,251))


# print(lista3)





## EXERCÍCIOS SOBRE LISTAS:

# **Exercício 0:** Escreva um programa que use a função `range()` 
# para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
# num = []
# num.range()
# print(num)

# lista =  list(range(2, 22, 4))
# print(lista)

# # **Exercício 1:** Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# print(numeros)

# # **Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.
# print(numeros[2])

# # **Exercício 3:** Adicione o número 9 à lista `numeros` e imprima a lista atualizada.
# numeros.append(9)
# print(numeros)
# # **Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.
# numeros.remove(4)
# print(numeros)

# # **Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.print(numer)
# carros = ["uno", "gol", "prisma"]
# lista = numeros + carros
# print(lista)


# listas = só com colchete 

# tuplas só com colchete

# conjuntos só com chaves 

