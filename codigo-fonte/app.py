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
        return f'{self.__saldo}'
    
    def get_limite(self):
        return f'{self.__limite}'
    
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self,valor):
        if valor > 0 and self.__saldo > 0:
            self.__saldo -= valor
            return valor
