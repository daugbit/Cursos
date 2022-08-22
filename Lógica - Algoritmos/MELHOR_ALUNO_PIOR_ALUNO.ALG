Algoritmo "melhor_aluno_pior_aluno"


Var
aluno, melhor_aluno, pior_aluno: caractere
n_alunos, cont: inteiro
nota, melhor_nota, pior_nota: real

Inicio
      escreval ("Escola Sem Futuro")
      escreval ("-----------------")
      escreva ("Quantos alunos a escola tem? ")
      leia (n_alunos)
      escreval ("-----------------")
      melhor_nota <- 0
      pior_nota <- 10
      melhor_aluno <- "Fulano"
      pior_aluno <- "Ciclano"
      cont <- 1
      enquanto (n_alunos > 0) faca
               escreval ("ALUNO ", cont)
               escreva ("Nome do aluno: ")
               leia (aluno)
               escreva ("Nota de ", aluno, ": ")
               leia (nota)
               escreval ("----------------------")
               se (nota > melhor_nota) entao
                  melhor_aluno <- aluno
                  melhor_nota <- nota
               fimse
               se (nota < pior_nota) entao
                  pior_aluno <- aluno
                  pior_nota <- nota
               fimse
               n_alunos <- n_alunos - 1
               cont <- cont + 1
      fimenquanto
      escreval ("O aluno com o melhor desempenho foi ", melhor_aluno, ", com nota ", melhor_nota, ".")
      escreval ("O aluno com o pior desempenho foi ", pior_aluno, ", com nota ", pior_nota, ".")
      escreval ("----------------------")
      


Fimalgoritmo