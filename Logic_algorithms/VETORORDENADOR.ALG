Algoritmo "VetorOrdenador"

Var
num: vetor[1..10] de inteiro
i, j, aux: inteiro

Inicio
      Para i de 1 ate 10 faca
           Escreva("Informe um número: ")
           Leia(num[i])
      FimPara

      Para i de 1 ate 9 faca
           Para j de i+1 ate 10 faca
                Se (num[j] < num[i]) entao
                   aux <- num[j]
                   num[j] <- num[i]
                   num[i] <- aux
                FimSe
           FimPara
      FimPara
      
      Para i de 1 ate 10 faca
      Escreva("{", num[i], "}")
      FimPara



Fimalgoritmo