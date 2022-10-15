# Functions

a <- 20
b <- 35
first_name <- 'Marcos'
last_name <- 'Cardoso'

c <- c(a,b)
c
?c

d <- c(10,20,30,40,50,100,1000)
summary(d)

full_name <- c(first_name,last_name)
full_name
summary(full_name)

# PACOTES
install.packages('stringr')
library(stringr)
full_name_form <- str_c(first_name, ' ', last_name)
full_name_form

# FUNÇÕES NUMÉRICAS
salario <- 3500.5
horas <- 220
sh <- salario / horas
shi <- as.integer(salario / horas)
diario <- shi * 8
sh <- round(salario / horas)

# CATEGORIZAÇÃO
itens <- c(100,100,220,500,500,500)
summary(itens)
categorias <- as.factor(itens)
summary(categorias)

is.vector(itens)
mode(itens)

# VETORES, LISTAS E MATRIZES
a <- c(1,2,3,4,5)
b <- c('1',2,3,4,'5')
is.vector(b)
is.list(b)
c <- as.numeric(b)

d <- list('1',2,3,4,'5')
is.list(d)
str(d)

e <- list(1,2,c('a','b','c'),c(3,4,5))
e[[3]][2]

m <- matrix(1:16, nrow = 4)
m
mode(m)
class(m)
m[3,2]
m[3,2] <- 10
m
m[3,2] <- 'R'
m
mode(m)

















