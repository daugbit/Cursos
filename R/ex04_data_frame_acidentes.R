setwd('/home/douglas/Downloads')
df_ibge <- read.csv('ibge.csv')

setwd('/home/douglas/Documents/GitHub/Cursos/R')
df_detran <- read.csv('AcidentalidadeRS.csv')

df_detran$População <- NA

df_ibge <- df_ibge[c(1, 6)]

i <- 1
while (i < 494) {
  j <- 1
  while (j < 497) {
    if (df_detran$Qtde.Vítimas[i] == df_ibge$Município....[j]) {
      df_detran$População[i] <- df_ibge$População.estimada...pessoas..2021.[j]
    }
    j <- j+1
  }
  i <- i+1
}

df_detran$População[492] <- 17126

df_detran <- df_detran[-493,]

df_filtrado <- df_detran[df_detran$População > 50000,]
df_filtrado <- df_filtrado[df_filtrado$População < 100000,]
