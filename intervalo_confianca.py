# ---------------------- #
#   ** BigData 4B  **    #
#    ╔═╗╔═╗╔╦╗╔═╗╔═╗     #
#    ╠╣ ╠═╣ ║ ║╣ ║       #
#    ╚  ╩ ╩ ╩ ╚═╝╚═╝     #
#    ** Ipiranga  **     #
#  << we take pride >>   #
# ---------------------- #

# Estudo de como calcular 
# intervalo de confiança usando Python.

# -------------------------------------------------------
# Problema apresentado na Aula de Estatistica - 19/09/24
# Prof. Silvio 
# Aula sobre Indice de Confiança
# -------------------------------------------------------

# utilizando a biblioteca scipy 
# para fazer a parte de estatística
import scipy.stats as st
import numpy

# O problema: 
# -----------
# Numa amostra de 75 consumidores foi colhida em 
# um shopping center mall para estimar a média de
# cartões de crédito que esses consumidores possuem
# A média da amostra é 4.3 cartões e o desvio padrao 
# da populaçao é 2.1 
# Qual o intervalo de confiança de 95% p/ a média
# do número de cartões de crédito dos consumidores ?

# ------------------------
#  Variaveis do Problema:
# ------------------------
desvio_padrao = 2.1 
n = 75 # Amostra - consumidores
media_amostra = 4.3 # media da amostra
ic = 0.95 # intervalo de confiança 

# primeiro, calculamos o erro_padrao 
erro_padrao = desvio_padrao/(n**0.5)

# Utilizo aqui a função interval da lib scipi 
# calcula o intervalo de confiança
# Passando as variaveis descritas acima ...
intervalos = st.t.interval(confidence=ic,df=n,loc=media_amostra,scale=erro_padrao)

# Resultado esperado : 
# (3.8169408998318475, 4.783059100168152)
print("\n\n Intervalos de confiança ")
print(intervalos,'\n\n')