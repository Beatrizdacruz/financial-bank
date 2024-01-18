from Conta import *
from Cliente import *
cliente1	=	Cliente('João',	'Oliveira',	'11111111111-11')
cliente2	=	Cliente('José',	'Azevedo',	'222222222-22')
conta1	=	Conta('123-4',	cliente1,	1000.0, 5000)
conta2	=	Conta('123-5',	cliente2,	1000.0, 2000)
conta1.deposita(100.0)
conta1.sacar(50.0)
conta1.transferePara(conta2,	200.0)
conta1.extrato
conta1.historico.retornaHistorico()
conta2.historico.retornaHistorico()

