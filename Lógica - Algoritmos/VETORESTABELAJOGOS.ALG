Algoritmo "VetoresTabelaJogos"


Var
time: vetor[1..4] de caractere
i, j: inteiro


Inicio
      Para i de 1 ate 4 faca
           Escreva(i, "º time: ")
           Leia(time[i])
      FimPara

      LimpaTela
      Escreval("--------------------------")
      Escreval("     TABELA DE JOGOS      ")
      Escreval("--------------------------")
      Para i de 1 ate 3 faca
           Para j de i+1 ate 4 faca
                Escreval(time[i]:15, "[ ]  x  [ ]":15, time[j])
                Escreval(time[j]:15, "[ ]  x  [ ]":15, time[i])
           FimPara
      FimPara




Fimalgoritmo