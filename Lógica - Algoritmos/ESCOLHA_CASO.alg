Algoritmo "semnome"


Var
nome, categoria: caractere
idade: inteiro


Inicio
      Escreval ("Informe o nome do atleta: ")
      Leia (nome)
      Escreval ("Informe a idade do atleta: ")
      Leia (idade)
      
      Escolha idade
              caso 17, 18, 19
                   categoria <- ("Categorias de base")
              caso 20, 21, 22
                   categoria <- ("Semi profissional")
              caso 23, 24, 25
                   categoria <- ("Profissional")
              outrocaso
                   categoria <- ("FALSO")
      Fimescolha

      Se (categoria = "FALSO") entao
         Escreval ("O atleta ", nome, " não se encaixa em nenhuma categoria")
      Senao
         Escreval ("O atleta ", nome, ", de ", idade, " anos, pertence à categoria ", categoria)
      Fimse


Fimalgoritmo