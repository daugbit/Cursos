# Configurando um local de trabalho (localização do arquivo fonte)
setwd('/home/douglas/Documents/GitHub/Cursos/R')

# Definindo o arquivo fonte
df <- read.csv('AcidentalidadeRS.csv')

# Exibindo e resumindo os dados
summary(df)
view(df)
str(df)
df$Municipal
summary(df$Municipal)
str(df$Municipal)

# Filtrando os dados
df[df$Federal > 3]


# Copiando o data frame
df2 <- df

# Manipulando os dados do data frame
df2$NÃO.INF. <- NULL
df2$NOVA <- 'TESTE'
df2$NOVA <- 'TESTE 2'
df2$NOVA[1:100] <- 'TESTE 3'
df2$NOVA <- NA
df2$NOVA[1:3] <- c('T1', 'T2', 'T3')

