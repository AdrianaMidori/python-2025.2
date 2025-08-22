# Strings
variavel_string = "python"
variavel_string2 = "uma linguagem 'facil'"

print(variavel_string)
print(variavel_string2)

print(len(variavel_string))
print(len(variavel_string2))

print(variavel_string2[0])
print(variavel_string2[2:7])
print(variavel_string2[-1])

print(type(variavel_string))

print("SPLIT")
print(variavel_string2.split())

print('DIR')
print(dir(variavel_string2))

print('LISTA')
outra_lista = ["casa", 5, "e", [4, 5, 6]]
print(outra_lista)
print(outra_lista[1])
print(outra_lista[2])
print(outra_lista[3])
print(outra_lista[3][2])

print("APPEND") #adiciona um elemento na lista
exemplo = [1, 6, 9, 10]
print(exemplo)
print(exemplo.append(8))
print(exemplo)

print("POP") #remove o último elemento da lista
exemplo = [1, 6, 9, 10]
print(exemplo)
print(exemplo.pop())
print(exemplo)

print("LISTA ORDENADA") #precisa ser do mesmo tipo
ordem = ["d", "a", "c", "z"]
print(ordem)
ordem.sort()
print(ordem)
ordem.reverse()
print(ordem)

print("DICIONARIO")
meu_dicionario = {"nome" : "Camila"}
print(meu_dicionario)

meu_dicionario = {"nome" : "Camila", "idade" : 29}
print(meu_dicionario["nome"])
#meu_dicionario = ["cidade"] = "Rio de Janeiro"
