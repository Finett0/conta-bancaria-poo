# Conta Bancária

Este projeto contém a implementação de uma classe `Conta` em Python, que simula o comportamento de uma conta bancária. A classe possui funcionalidades como depósito, saque, transferência e exibição de detalhes da conta.

## Funcionalidades

- **Criar uma conta bancária** com número da conta, titular, saldo e limite.
- **Depósito**: Adicionar fundos à conta.
- **Saque**: Retirar dinheiro da conta, verificando se há saldo suficiente.
- **Transferência**: Transferir valores para outra conta (simulação).
- **Exibir Detalhes**: Mostrar as informações da conta, incluindo saldo e limite.

## Estrutura do Projeto

### Atributos

A classe `Conta` possui os seguintes atributos:
- `__numero_conta`: Número da conta (privado).
- `__titular`: Nome do titular da conta (privado).
- `__saldo`: Saldo disponível (privado).
- `__limite`: Limite do cheque especial (privado).
- `agencia`: Agência padrão (`0001`).

### Métodos

#### Métodos de Acesso
- `get_numero_conta()`: Retorna o número da conta.
- `get_titular()`: Retorna o nome do titular.
- `get_saldo()`: Retorna o saldo formatado.
- `get_limite()`: Retorna o limite formatado.

#### Operações
- `depositar(valor)`: Adiciona um valor ao saldo, caso seja positivo.
- `sacar(valor)`: Subtrai um valor do saldo, caso haja saldo suficiente.
- `transferir(valor)`: Realiza a transferência de valores entre contas (simulação).
- `exibir_detalhes()`: Retorna uma string com os detalhes da conta.

## Exemplo de Uso

```python
# Criando uma conta bancária
conta1 = Conta(numero_conta=1234, titular="João Silva", saldo=1000.00, limite=500.00)

# Exibindo os detalhes da conta
print(conta1.exibir_detalhes())

# Realizando um depósito
conta1.depositar(500.00)
print(conta1.get_saldo())  # Saldo atualizado

# Realizando um saque
print(conta1.sacar(200.00))

# Tentando sacar mais do que o saldo disponível
print(conta1.sacar(2000.00))

# Transferência de valores
conta1.transferir(300.00)
