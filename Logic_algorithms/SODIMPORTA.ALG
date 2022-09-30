Algoritmo "SoDImporta"


Var
i, tot: inteiro
nome, SoD: vetor[1..10] de caractere
totD: vetor[1..10] de inteiro


Inicio
      tot <- 0
      Para i de 1 ate 10 faca
           Escreva(i, "º nome: ")
           Leia(nome[i])
           Se (copia(maiusc(nome[i]), 1, 1) = "D") entao
              tot <- tot + 1
              SoD[tot] <- nome[i]
           FimSe
      FimPara

      Escreval("-------------------------")
      Escreval("Entre os nomes informados, ", tot, " começam com a letra D:")
      Para i de 1 ate tot faca
           Escreval(SoD[i])
      FimPara


Fimalgoritmo