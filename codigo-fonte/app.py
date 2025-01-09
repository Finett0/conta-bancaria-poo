import os

class Conta:
    def __init__(self,numero_conta,titular,saldo,limite):
        self.__numero_conta = numero_conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.agencia = '0001'

    def get_numero_conta(self):
        return f'{self.__numero_conta}'
    
    def get_titular(self):
        return f'{self.__titular}'
    
    def get_saldo(self):
        return f'R${self.__saldo}'
    
    def get_limite(self):
        return f'R${self.__limite}'
    
    
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return f'O saque de R${valor} foi feito com sucesso seu saldo agora é de {self.get_saldo()}'
        else:
            return f'{self.get_titular()},não foi possivel efetuar o saque pelo motivo: Saldo Insuficiente'

    def transferir(self,valor):
        if self.__saldo >= valor:
            self.sacar(valor)
            print(f'Transferencia de R${valor} realizada com sucesso!')
        else:
            print(f'Transferencia de R${valor} não realizada, Saldo insuficiente.')

    def exibir_detalhes(self):
        os.system('cls')
        return f'Detalhes da conta {self.get_numero_conta()}\n---------------------------------\nNome: {self.get_titular()}\nAgencia: {self.agencia}\nSaldo: {self.get_saldo()}\nLimite Cheque Especial: {self.get_limite()}'




pessoa1 = Conta(22234,'Giovanni Finetto',1000,200)
detalhes = pessoa1.exibir_detalhes()
print(detalhes)

pessoa1.transferir(1000)
print(f'\nO seu saldo agora é de {pessoa1.get_saldo()}')

print(f'{pessoa1.get_titular()}, {saque1}')
saque2 = pessoa1.sacar(950)
print(f'{saque2}')
