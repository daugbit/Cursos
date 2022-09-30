Algoritmo "repita_ate"


Var
aluno: caractere
n1, n2, n3, MH, i: real

Inicio
i <- 1
repita
      escreval ("Informe o nome do aluno: ")
      leia (aluno)
      escreval ("Informe a nota 1 do aluno ", aluno, ": ")
      leia (n1)
      escreval ("Informe a nota 2 do aluno ", aluno, ": ")
      leia (n2)
      escreval ("Informe a nota 3 do aluno ", aluno, ": ")
      leia (n3)
      MH <- 3/(1/n1 + 1/n2 + 1/n3)
      escreval ("A média harmônica do aluno ", aluno, " é: ", MH:1:1)
      i <- (i + 1)
ate i > 3

Fimalgoritmo