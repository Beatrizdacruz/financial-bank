import datetime

class Historico:
    def __init__(self):
        """Armazena o histórico de um usuário referente à sua conta.
        Alguns pontos a melhorar: 
        - classificar as operações como tranferencia, deposito, entrada ou saída;
        - ter a data de cada transação;
        """
        self.dataAbertura = datetime.datetime.today()
        self.transacoes = []
    
    def retornaHistorico(self):
        print(f'Abertura de conta: {self.dataAbertura}')
        print('Transações realizadas:')
        for transacao in self.transacoes:
            print('-' + transacao)