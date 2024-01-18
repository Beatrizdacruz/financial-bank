from Historico import *
class Conta:
    #TODO
    def	__init__(self,	numero,	cliente, saldo, limite):

        self.numero	= numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()



    def criar_conta(self, numero, titular, saldo, limite):
        """
        Cria uma nova conta bancária.

        Parâmetros:
        - numero (int): Número da conta.
        - titular (str): Nome do titular da conta.
        - saldo (float): Saldo inicial da conta.
        - limitee (float): limitee de crédito da conta.

        Retorna:
        Um dicionário representando a conta bancária.
        """
        conta = {'Número da conta:': numero,'Titular:': titular, 'Saldo:': saldo, 'limitee:': limite}
        print(f'conta criada com sucesso! Bem vindo(a), {titular}!')
        self.historico.transacoes.append('criação de conta')
        return conta

    def deposita(self, valor):
        """
        Deposita um valor na conta bancária.

        Parâmetros:
        - valor (float): Valor a ser depositado.
        """
        self.saldo += valor
        print(f'você depositou {valor}')
        self.historico.transacoes.append(f'Depósito de R${valor}')

    def sacar(self, valor):
        """
        Retira um valor da conta bancária.

        Parâmetros:
        - valor (float): Valor a ser retirado.
        """
        if self.saldo < valor:
            print('Não foi possível realizar a operação. Não há saldo suficiente.')
            return False
        else:
            self.saldo -= valor
            print(f'Você sacou {valor}. Seu saldo atual é de R${self.saldo}')
            self.historico.transacoes.append(f'Saque de R${valor}')
            return True

    def extrato(self):
        """
        Exibe o histórico da conta bancária.
        """
        print(f'Conta:{self.numero} \nSaldo: {self.saldo}')

    def	transferePara(self,	valor, contaDestino):
        """
        Realiza a retirada do valor de uma conta e a insere em outra.
        Parâmetros:
        - valor: valor a ser retirado da conta e enviado.
        - contaDestino: conta a ser enviada o valor.
        """
        retirada = self.sacar(valor)
        if retirada == True:
            self.deposita(valor)
            self.historico.transacoes.append(f'Transferência no valor de R${valor} para {contaDestino.numero}')
            return True
        else:
            print('Um problema ocorreu ao realizar a operação. Por favor, tente novamente em instantes.')
            return False
    
    # Teste da documentação usando help()
    if __name__ == "__main__":
        help(criar_conta)