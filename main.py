#Exercícios: Listas, Tuplas e Dicionários

#1.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

#legenda: a = aluno range 10 quantidade de alunos  no= nota range 4 quantidade de notas  listaNotas = [] serão guardadas as medias dos alunos

listaNotas = []
notasAluno = [] 
media_seteoumais = 0

print ('Calculando as notas dos Alunos e quantos estão acima de 7'+'\n')

for a in range(10):
  media = 0
  notasAluno = []
  print ('Aluno: ' + str(a + 1))
  
  for no in range(4):
    notasAluno.append(float(input('Nota: ' + str(no+1) + '\n')))
    media += notasAluno[no]
  print ("A sua nota total é:",media)
  media /= 4
  listaNotas.append(media)
  if media >= 7:
        media_seteoumais += 1
print("\nResultados finais:")
print(f"\nAs médias dos alunos são:",listaNotas)
print(f"\n{media_seteoumais} alunos tiveram média maior ou igual a 7.")


#2. Programa nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

print ("Digite o seu nome e veja o programa deixá-lo escrito ao contrário e com todas as letras maiúsculas. Para ver a mágica acontecer, digite o seu nome utilizando letras maiúsculas ou minúsculas e após dar o 'enter' aguarde a mágica!")

nome_orig = (input("\nDigite o seu nome:"))
maiusculo = nome_orig.upper()
inv_maiusculo = maiusculo[::-1]
print("Pronto: esse é o seu nome com todas as letras maiúsculas e invertido:",inv_maiusculo)

#3. Escreva um programa em Python que onde todos os valores em um dicionário são emitidos. Se sim , imprima True. Caso contrário, imprima Falso.

#4. "Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
#As perguntas são:
#""Telefonou para a vítima?""
#""Esteve no local do crime?""
#""Mora perto da vítima?""
#""Devia para a vítima?""
#"Já trabalhou com a vítima?""


#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"". Caso contrário, ele será classificado como ""Inocente"".