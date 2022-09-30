Algoritmo "SoftwareMasterCompleto"

Var
   inic: caractere



   //////////////PROCEDIMENTOS///////////////////

Procedimento SelecaoSoftware()
Var
   app: inteiro
Inicio
   LimpaTela
   Escreval("---------------------------------------------")
   Escreval("           SOFTWARE MASTER COMPLETO          ")
   Escreval("---------------------------------------------")
   Escreval("[1] Fibonacci")
   Escreval("[2] Números primos")
   Escreval("[3] Tabuada")
   Escreval("[4] Fatorial")
   Escreval("[5] Calculadora IMC")
   Escreval("[6] Calculadora de comida para festas")
   Escreval("[7] Panorama de notas da turma")
   Escreval("[8] Verificação de categoria atletas")
   Escreval("[9] ENCERRAR SOFTWARE")
   Escreval("---------------------------------------------")
   Escreva("Escolha o aplicativo que você quer executar: ")
   Leia (app)
   Escolha app
   Caso 1
      Fibonacci()
   Caso 2
      NumerosPrimos()
   Caso 3
      Tabuada()
   Caso 4
      Fatorial()
   Caso 5
      IMC()
   Caso 6
      ComidaFestas()
   Caso 7
      Notas()
   Caso 8
      CatAtletas()
   Caso 9
      TelaFinal()
   Outrocaso
      Escreval("Opção inválida. Reinicie o aplicativo.")
   FimEscolha
FimProcedimento

/////////////////////////////////////

Procedimento Fibonacci()
Var
   N1, N2, N3, R, C: inteiro
   c, final: caractere
Inicio
   Repita
      LimpaTela
      Escreva ("Quantos números da sequência de Fibonacci você quer ver? ")
      Leia (R)
      N1 <- 0
      N2 <- 1
      Escreval(N1)
      Escreval(N2)
      para C de 1 ate (R-2) faca
         N3 <- N1 + N2
         Escreval (N3)
         N1 <- N2
         N2 <- N3
      fimpara
      Escreva(
      escreval("----------------------------------")
      escreva("Deseja repetir o processo? [s/n]  ")
      leia(c)
   ate (c="n")
   LimpaTela
   Escreva("Deseja iniciar outro aplicativo? [s/n]")
   Leia(final)
   Se (final = "s") entao
      SelecaoSoftware()
   Senao
      TelaFinal()
   FimSe
FimProcedimento

/////////////////////////////////////

Procedimento NumerosPrimos()
Var
   cont1, cont2, NI, ContDiv, primo: inteiro
   c, final: caractere
Inicio
   repita
      LimpaTela
      escreval ("--------------------------------------------")
      escreval ("   ANALISADOR DE NÚMEROS PRIMOS  ")
      escreval ("  Digite um número e descubra todos")
      escreval ("     os números primos até ele")
      escreval ("--------------------------------------------")
      cont2 <- 1
      primo <- 1
      escreva ("Informe o número: ")
      leia (NI)
      escreval ("--------------------------------------------")
      escreval ("Estes são os números primos até ", NI, ":")
      escreval (" ")
      repita
         cont1 <- 1
         ContDiv <- 0
         repita
            se (primo % cont1 = 0) entao
               ContDiv <- ContDiv + 1
            fimse
            cont1 <- cont1 + 1
         ate (cont1 > primo)
         se (ContDiv <= 2) entao
            escreval (primo)
         fimse
         primo <- primo + 1
         cont2 <- cont2 +1
      ate (cont2 > NI)
      escreval("----------------------------------")
      escreva("Deseja repetir o processo? [s/n]  ")
      Leia(c)
   ate(c="n")
   LimpaTela
   Escreva("Deseja iniciar outro aplicativo? [s/n]")
   Leia(final)
   Se (final = "s") entao
      SelecaoSoftware()
   Senao
      TelaFinal()
   FimSe
FimProcedimento

/////////////////////////////////////

Procedimento Tabuada()
Var
   n, r: inteiro
   c, final: caractere
Inicio
   repita
      LimpaTela
      escreva ("Informe o número da tabuada: ")
      leia (r)
      n <- 1
      repita
         escreval (r, " x ", n, " = ", r*n)
         n <- n + 1
      ate (n > 10)
      escreval("----------------------------------")
      escreva("Deseja repetir o processo? [s/n]  ")
      leia (c)
   ate (c = "n")
   LimpaTela
   Escreva("Deseja iniciar outro aplicativo? [s/n]")
   Leia(final)
   Se (final = "s") entao
      SelecaoSoftware()
   Senao
      TelaFinal()
   FimSe
FimProcedimento

/////////////////////////////////////

Procedimento Fatorial()
Var
   cont, f, num: inteiro
   c, final: caractere
Inicio
   repita
      LimpaTela
      escreva ("Informe o número: ")
      leia (num)
      f <- 1
      cont <- 1
      repita
         f <- f*cont
         cont <- cont + 1
      ate (cont>num)
      limpatela
      escreval ("O fatorial de ", num, " é ", f)
      escreval("----------------------------------")
      escreva("Deseja repetir o processo? [s/n]  ")
      leia(c)
   ate(c="n")
   LimpaTela
   Escreva("Deseja iniciar outro aplicativo? [s/n]")
   Leia(final)
   Se (final = "s") entao
      SelecaoSoftware()
   Senao
      TelaFinal()
   FimSe
FimProcedimento

/////////////////////////////////////

Procedimento IMC()
Var
   massa, altura, indice: Real
   c, final: caractere
Inicio
   Repita
      LimpaTela
      Escreva("Informe seu peso (kg): ")
      Leia(massa)
      Escreva("Informe a sua altura (m): ")
      Leia(altura)
      indice <- massa / altura^2
      Escreval("--------------------------------")
      Escreval("Seu IMC é ", indice:5:2)
      Se (indice <= 17) entao
         Escreval("Você está abaixo do seu peso ideal)
      Senao
         Se (indice > 17) e (indice <= 25) entao
            Escreval ("Você está no seu peso ideal")
         Senao
            Se (indice > 25) e (indice <= 30) entao
               Escreval("Você está com sobrepeso")
            Senao
               Se (indice > 30) e (indice <= 35) entao
                  Escreval("Você está com obesidade nível I")
               Senao
                  Se (indice > 35) e (indice <= 40) entao
                     Escreval("Você está com obesidade nível II")
                  Senao
                     Escreval("Você está com obesidade mórbida")
                  FimSe
               FimSe
            FimSe
         FimSe
      FimSe
      escreval("----------------------------------")
      escreva("Deseja repetir o processo? [s/n]  ")
      leia(c)
   ate(c="n")
   LimpaTela
   Escreva("Deseja iniciar outro aplicativo? [s/n]")
   Leia(final)
   Se (final = "s") entao
      SelecaoSoftware()
   Senao
      TelaFinal()
   FimSe

FimProcedimento

/////////////////////////////////////

Procedimento ComidaFestas()
Inicio

FimProcedimento

/////////////////////////////////////

Procedimento Notas()
Var
   c, final, aluno, melhor_aluno, pior_aluno: caractere
   n_alunos, cont: inteiro
   nota, melhor_nota, pior_nota: real

Inicio
   repita
      limpatela
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
      escreval("----------------------------------")
      escreva("Deseja repetir o processo? [s/n]  ")
      leia(c)
   ate(c="n")
   LimpaTela
   Escreva("Deseja iniciar outro aplicativo? [s/n]")
   Leia(final)
   Se (final = "s") entao
      SelecaoSoftware()
   Senao
      TelaFinal()
   FimSe
FimProcedimento

/////////////////////////////////////

Procedimento CatAtletas()
Var
   c, final, nome, categoria: caractere
   idade: inteiro


Inicio
   repita
      limpatela
      Escreva("Informe o nome do atleta: ")
      Leia (nome)
      Escreva("Informe a idade do atleta ", nome, ": ")
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
         escreval("----------------------------------")
         Escreval ("O atleta ", nome, " não se encaixa em nenhuma categoria")
      Senao
         escreval("----------------------------------")
         Escreval ("O atleta ", nome, ", de ", idade, " anos, pertence à categoria ", categoria)
      Fimse
      escreval("----------------------------------")
      escreva("Deseja repetir o processo? [s/n]  ")
      leia(c)
   ate(c="n")
   LimpaTela
   Escreva("Deseja iniciar outro aplicativo? [s/n]")
   Leia(final)
   Se (final = "s") entao
      SelecaoSoftware()
   Senao
      TelaFinal()
   FimSe
FimProcedimento

/////////////////////////////////////

Procedimento TelaFinal()
Inicio
   LimpaTela
   Escreval("---------------------------------------------")
   Escreval("            Obrigado por utilizar o          ")
   Escreval("           SOFTWARE MASTER COMPLETO          ")
   Escreval("---------------------------------------------")
FimProcedimento


///////////FIM PROCEDIMENTOS///////////////////




Inicio
   Escreval("---------------------------------------------")
   Escreval("                 Bem-vindo ao                ")
   Escreval("           SOFTWARE MASTER COMPLETO          ")
   Escreval("---------------------------------------------")
   Escreval("")
   Escreval("      Tecle ENTER para acessar as opções     ")
   Leia (inic)
   SelecaoSoftware()



Fimalgoritmo