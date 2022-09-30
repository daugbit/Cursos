Algoritmo "Matriz_Opcoes"


Var
   mat: vetor[1..4,1..4] de inteiro
   i, j, op: inteiro

   ///////////////////////PROCEDIMENTOS///////////////

Procedimento TelaOpcoes()
Inicio
   Escreval("-----------------------------")
   Escreval("[1] Exibir matriz")
   Escreval("[2] Exibir diagonal principal")
   Escreval("[3] Exibir triângulo superior")
   Escreval("[4] Exibir triângulo inferior")
   Escreval("[5] SAIR")
   Escreval("-----------------------------")
   Escreva("Escolha uma das opções:")
   Leia(op)

   Escolha op
   Caso 1
      LimpaTela
      MatrizPrincipal()
   Caso 2
      LimpaTela
      DiagonalPrincipal()
   Caso 3
      LimpaTela
      TrianguloSuperior()
   Caso 4
      LimpaTela
      TrianguloInferior()
   Caso 5
      LimpaTela
      Escreval("ENCERRANDO...")
   FimEscolha
FimProcedimento


Procedimento MatrizPrincipal()
Inicio
   Escreval("MATRIZ PRINCIPAL:")
   Escreval("-----------------")
   Para i de 1 ate 4 faca
      Para j de 1 ate 4 faca
         Escreva(mat[i,j])
      FimPara
      Escreval()
   FimPara
   TelaOpcoes()
FimProcedimento


Procedimento DiagonalPrincipal()
Inicio
   Escreval("DIAGONAL PRINCIPAL:")
   Escreval("-----------------")
   Para i de 1 ate 4 faca
      Para j de 1 ate 4 faca
         Se (i = j) entao
            Escreva(mat[i,j])
         Senao
            Escreva("  ")
         FimSe
      FimPara
      Escreval()
   FimPara
   TelaOpcoes()
FimProcedimento


Procedimento TrianguloSuperior()
Inicio
   Escreval("TRIANGULO SUPERIOR:")
   Escreval("-----------------")
   Para i de 1 ate 4 faca
      Para j de 1 ate 4 faca
         Se (i < j) entao
            Escreva(mat[i,j])
         Senao
            Escreva("  ")
         FimSe
      FimPara
      Escreval()
   FimPara
   TelaOpcoes()
FimProcedimento


Procedimento TrianguloInferior()
Inicio
   Escreval("TRIANGULO SUPERIOR:")
   Escreval("-----------------")
   Para i de 1 ate 4 faca
      Para j de 1 ate 4 faca
         Se (i > j) entao
            Escreva(mat[i,j])
         Senao
            Escreva("  ")
         FimSe
      FimPara
      Escreval()
   FimPara
   TelaOpcoes()
FimProcedimento


///////////////////////FIM_PROCEDIMENTOS///////////////

Inicio
   Para i de 1 ate 4 faca
      Para j de 1 ate 4 faca
         Escreva("Informe o valor da posição [", i, ",", j, "]: ")
         Leia(mat[i,j])
      FimPara
   FimPara

   LimpaTela
   
   TelaOpcoes()

Fimalgoritmo