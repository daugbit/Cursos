Algoritmo "VetoresReservaCinema"


Var
   P: vetor[1..10] de inteiro
   i, x: inteiro
   R: caractere


Procedimento TelaPoltronas()
Inicio
   LimpaTela
   Escreval("SISTEMA DE RESERVAS DO CINEMATOP")
   Escreval("-------------------------------------------------")
   Para i de 1 ate 10 faca
      Se (P[i] = 0) entao
         Escreva("[B", i, "] ")
      SeNao
         Escreva("[--] ")
      FimSe
   FimPara
FimProcedimento


Inicio

   Para i de 1 ate 10 faca
      P[i] <- 0
   FimPara

   //Valores atribuídos a "x" representam poltrona disponível (0) e ocupada (1)
   x <- 0

   Repita
      TelaPoltronas()
      Escreval("")
      Escreval("-------------------------------------------------")
      Escreva("Informe a poltrona que você deseja reservar: B")
      Leia(x)
      Se (P[x] = 0) entao
         P[x] <- 1
      SeNao
         Escreval("ERRO! Esta poltrona já está reservada")
         Escreval("Tecle ENTER para selecionar outra poltrona")
         Leia(R)
      FimSe
      TelaPoltronas()
      Escreval("")
      Escreval("-------------------------------------------------")
      Escreva("Deseja reservar outra poltrona? [s/n] ")
      Leia(R)
   Ate (R = "n")



Fimalgoritmo