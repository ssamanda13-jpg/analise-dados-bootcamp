#abertura do sistema
print("Bem vindo a aula de python, vamos aprender a trabalhar com variáveis, listas e dicionários.\n")

nome_usuario = "Amanda"
# essa memória é do tipo str: (texto)
senha_usuario = "123"
# essa memória é do tipo int: (número inteiro)

#tipos de memória
#texto - sempre entre aspas ""
#numero inteiro
#numero decimal

#mostrando na tela
print("usuario",nome_usuario)
print("senha",senha_usuario)

#Atividade 1
#Criando uma persona
print("Vamos criar uma persona?")

#Criar variáveis
nome_persona = input("Informe o nome da persona")
# se eu uso o input apenas, a informação armazena na variável será um texto

idade_persona = int(input("qual sua idade?"))
#ao combinar o comando int() com o comando input() - int(input()) - eu armazeno uma resposta como um numero inteiro

altura_persona = float(input("informe sua altura"))
#Ao combinar o comando float () com o comando input() - float(input()) - armazenamos a resposta com um número decimal

#três tipos de dadis (data types)
#str - para textos
#int - ára números inteiros 
#float - para números decimais 

print("Olá",nome_persona,"você tem",idade_persona,"anos e",altura_persona,"metros de altura")
#Olá Adilson, você tem XX anos e YY metros de altura

#Operações simples
falta_100 = 100 - idade_persona

print("Faltam", falta_100,"para chegar aos 100 anos de idade")
#NOME DA PESSOA, faltam XX anos

print(type(falta_100))
#O comando type serve para descobrir o tipo de dado

# Tipois e conversão 
falta_100_txt = str(falta_100)
print(type(falta_100_txt))

#lista - basicamente é uma variavel que suporta muitos valores
aluno = ["Pedro J","Rhayna L","Daniel C","Luiz A"]

print(aluno)
#Se eu uso nome de lista apenas, eu vou exibir todos os seu elementos

print(aluno[2])
#Posso então utilizar o index do elemento da lista, para chamar ele

print(aluno[2])
#Posso então utilizar o index do elemente na lista, para chamar ele 

print(aluno[-1])

#Dicionário
pessoa = {"nome":"Luiz", "idade":31,"cidade":"Iguape"}

print(pessoa)

print(pessoa.keys())

print(aluno)

aluno.append("Ana M.")

print("Lista Atualizada:",aluno)

print("O total de pessoas cadastradas são:", len(aluno))

print("Removendo Daniel do cadastro")

aluno.remove("Daniel C")

print("Total de alunos agora", len(aluno))






