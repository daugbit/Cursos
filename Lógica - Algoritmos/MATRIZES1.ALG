Algoritmo "Matrizes1"


Var
Mat: vetor[1..3, 1..3] de inteiro
i, j: inteiro


Inicio
      Para i de 1 ate 3 faca
           Para j de 1 ate 3 faca
                Escreva("Digite o número da posição [", i, ",", j, "]: ")
                Leia(mat[i,j])
           FimPara
      FimPara
      
      Escreval()
      Escreval("MATRIZ FINAL")
      Escreval("------------")
      Para i de 1 ate 3 faca
           Para j de 1 ate 3 faca
                Escreva(mat[i,j])
           FimPara
           Escreval()
      FimPara
      


Fimalgoritmo