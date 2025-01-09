class Conta:
    def __init__(self,numero_conta,titular,saldo,limite):
        self.__numero_conta = numero_conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def get_numero_conta(self):
        return f'{self.__numero_conta}'
    
    def get_titular(self):
        return f'{self.__titular}'
    
    def get_saldo(self):
        return f'R${self.__saldo}'
    
    def get_limite(self):
        return f'{self.__limite}'
    
    
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return f'O saque de R${valor} foi feito com sucesso seu saldo agora é de {self.get_saldo()}'
        else:
            return f'{self.get_titular()},não foi possivel efetuar o saque pelo motivo: Saldo Insuficiente'

    def transferir(self,valor,conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            print(f'Transferencia de R${valor} realizada com sucesso!')
        else:
            print(f'Transferencia de R${valor} não realizada, Saldo insuficiente.')




pessoa1 = Conta(22234,'Giovanni Finetto',1000,200)
print(f'Olá {pessoa1.get_titular()} seu saldo atual é de {pessoa1.get_saldo()}')
saque1 = pessoa1.sacar(950)
print(f'{pessoa1.get_titular()}, {saque1}')
saque2 = pessoa1.sacar(950)
print(f'{saque2}')
