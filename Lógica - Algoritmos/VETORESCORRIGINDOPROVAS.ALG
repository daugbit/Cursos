Algoritmo "VetoresCorrigindoProvas"


Var
aluno: vetor[1..40] de caractere
nota: vetor[1..40] de real
R, opcao: vetor[1..50] de caractere
i, q, a, p: inteiro
peso, tot, media: real


Inicio
   Escreva("Informe o número de alunos na turma: ")
   Leia(a)
   Escreva("Informe o número de questões da prova: ")
   Leia(p)
   Escreva("Informe o peso da prova: ")
   Leia(peso)

   LimpaTela

   Escreval("GABARITO DA PROVA")
   Escreval("------------------")
   Para i de 1 ate p faca
      Escreva("Questão ", i, ": ")
      Leia(R[i])
   FimPara

   LimpaTela
   Escreval("CORREÇÃO DAS PROVAS")
   Escreval("--------------------")

   tot <- 0
   
   Para i de 1 ate a faca
      LimpaTela
      Escreva("Aluno: ")
      Leia(aluno[i])
      nota[i] <- 0
      Para q de 1 ate p faca
           Escreva("Questão ", q, ": ")
           Leia(opcao[q])
           Se (opcao[q] = R[q]) entao
              nota[i] <- nota[i] + (peso/p)
           FimSe
      FimPara
      tot <- tot + nota[i]
   FimPara
   
   media <- tot/a

   LimpaTela
   Escreval("RESULTADOS FINAIS DA TURMA")
   Escreval("--------------------------")
   Para i de 1 ate a faca
        Escreval(aluno[i]:10, nota[i]:4:2)
   FimPara
   Escreval("--------------------------")
   Escreval("A média da turma foi: ", media:4:2)



Fimalgoritmo