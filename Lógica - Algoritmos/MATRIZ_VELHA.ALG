algoritmo "Matriz_Velha"

var
   resp, c, i, j, nj: inteiro
   JogadorAtual: caractere
   velha: vetor[1..3,1..3] de caractere
   jogada: vetor[1..9] de inteiro
   JogadaValida, FimJogo: logico

Procedimento AtualizaTela()
Inicio
   Escreval("+--+--+--+")
   para i de 1 ate 3 faca
      Escreva("|")
      para j de 1 ate 3 faca
         Escreva(velha[i,j]:2)
         Escreva("|")
      fimpara
      Escreval()
      Escreval("+--+--+--+")
   fimpara
FimProcedimento

Funcao VerificaJogada(resp: inteiro): logico
Inicio
   Se (resp = jogada[resp]) entao
      jogada[resp] <- 0
      retorne verdadeiro
   Senao
      Escreval("Jogada inválida!")
      retorne falso
   Fimse
FimFuncao

Procedimento RegistraJogada()
Inicio
   Escolha resp
   Caso 1, 2, 3
      velha[1, resp] <- JogadorAtual
   Caso 4, 5, 6
      velha[2, resp-3] <- JogadorAtual
   Caso 7, 8, 9
      velha[3, resp-6] <- JogadorAtual
   FimEscolha
FimProcedimento

Procedimento VerificaResultado()
Inicio
   Para j de 1 ate 3 faca
      Se (velha[1,j] = velha[2,j]) e (velha[2,j] = velha[3,j]) entao
         FimJogo <- verdadeiro
         LimpaTela
         AtualizaTela()
         Escreval()
         Escreval("FIM DE JOGO: O vencedor foi ", JogadorAtual)
      FimSe
   FimPara

   Se (nao FimJogo) entao
      Para i de 1 ate 3 faca
         Se (velha[i,1] = velha[i,2]) e (velha[i,2] = velha[i,3]) entao
            FimJogo <- verdadeiro
            LimpaTela
            AtualizaTela()
            Escreval()
            Escreval("FIM DE JOGO: O vencedor foi ", JogadorAtual)
         FimSe
      FimPara
   FimSe

   Se (nao FimJogo) entao
      Se (velha[1,1] = velha[2,2]) e (velha[2,2] = velha[3,3]) entao
         FimJogo <- verdadeiro
         LimpaTela
         AtualizaTela()
         Escreval()
         Escreval("FIM DE JOGO: O vencedor foi ", JogadorAtual)
      FimSe
   FimSe

   Se (nao FimJogo) entao
      Se (velha[1,3] = velha[2,2]) e (velha[2,2] = velha[3,1]) entao
         FimJogo <- verdadeiro
         LimpaTela
         AtualizaTela()
         Escreval()
         Escreval("FIM DE JOGO: O vencedor foi ", JogadorAtual)
      FimSe
   FimSe

   Se (nao FimJogo) entao
      Se (nj = 9) entao
         FimJogo <- verdadeiro
         LimpaTela
         AtualizaTela()
         Escreval()
         Escreval("FIM DE JOGO: Deu velha!")
      Senao
         nj <- (nj + 1)
      FimSe
   FimSe
FimProcedimento

Procedimento TrocaJogador()
Inicio
   Se (JogadorAtual = "X") entao
      JogadorAtual <- "O"
   Senao
      JogadorAtual <- "X"
   FimSe
FimProcedimento


Inicio
   c <- 1
   para i de 1 ate 3 faca
      para j de 1 ate 3 faca
         velha[i,j] <- numpcarac(c)
         c <- c + 1
      fimpara
   fimpara

   c<- 1
   para i de 1 ate 9 faca
      jogada[i] <- c
      c <- c + 1
   Fimpara

   JogadorAtual <- "X"
   nj <- 1

   Repita
      LimpaTela
      AtualizaTela()
      Repita
         Escreval()
         Escreva("Vai jogar ", JogadorAtual, " em qual posição? ")
         Leia(resp)
         JogadaValida <- VerificaJogada(resp)
      ate (JogadaValida = verdadeiro)

      RegistraJogada()

      VerificaResultado()

      TrocaJogador()
   ate (FimJogo = verdadeiro)

FimAlgoritmo