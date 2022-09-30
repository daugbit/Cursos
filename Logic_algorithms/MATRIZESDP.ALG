Algoritmo "MatrizesDP"


Var
Mat: vetor[1..3, 1..3] de inteiro
i, j: inteiro


Inicio

      Para i de 1 ate 3 faca
           Para j de 1 ate 3 faca
                Se (i = j) entao
                   mat[i,j] <- 1
                Senao
                   mat[i,j] <- 0
                FimSe
                Escreva(mat[i,j])
           FimPara
           Escreval()
      FimPara
      


Fimalgoritmo