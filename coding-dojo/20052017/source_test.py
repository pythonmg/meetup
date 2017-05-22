# Para cada sabor de pizza disponível, 
# cada um deve indicar uma nota para ele 
# (nota 1, se a pessoa detesta o sabor e nota 5 se a 
# pessoa adora o sabor). 
# Depois de processar esses dados, 
# cada pessoa vai saber quais as pessoas que 
# tem o gosto mais parecido que o seu 
# (e que provavelmente irá dividir uma pizza com você).
# Marguerita - Quatro queijos - Escarola
# Portuguesa - Frango+Catupiry - Napolitana

#  FUNCIONARIOS = {
#	CLAUDIO : {Marguerita: 1, Quatro_Queijos: 3}
#   CÁSSIO : {Marguerita: 5, Quatro_Queijos: 2}
#   ANDRE : {Marguerita: 4, Quatro_Queijos: 1}
#  }
 
# ANFITRIAO : {Marguerita: 4, Quatro_Queijos: 2}
# RETORNO =NOME DE UM DOS FUNCIONARIOS
from source import verifica_perfil





def test_verificar_perfil_marguerita():
	ANFITRIAO = {"Marguerita": 4}
	FUNCIONARIOS = {
	   "CLAUDIO" : {"Marguerita": 1},
	   "CÁSSIO" : {"Marguerita": 5},
	   # "ANDRE" : {"Marguerita": 4, "Quatro_Queijos": 1}
	 }
	assert verifica_perfil(ANFITRIAO, FUNCIONARIOS) == "CÁSSIO"

