class Cliente: # Informações básicas sobre o cliente
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
    
    @staticmethod
    def criar_cliente():
        nome = input('Digite o seu nome: ')
        cpf = input('Digite seu CPF: ')
        endereço = input('Digite o seu endereço: ')
        return Cliente(nome, cpf, endereço)
    
    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"


class Conta: # Aqui é onde teremos os métodos para sacar e depositar dinheiro
    def __init__(self, numero_conta, cliente):
        self.numero_conta = numero_conta
        self.saldo = 0.0 # Começa com saldo 0
        self.cliente = cliente

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito do valor {valor} efetuado com sucesso. Seu saldo agora é de R${self.saldo}')
        else:
            print('ERRO! O valor depositado tem que ser maior que 0')
    
           
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque do valor {valor} efetuado com sucesso. O seu saldo agora é de {self.saldo}')
        else:
            print('ERRO! Você não tem saldo suficiente')


    def consultar_saldo(self):
        print(f'O seu saldo atual é de {self.saldo}')
        return self.saldo
    
    @staticmethod
    def criar_conta(cliente):
        numero = input('Digite o número da conta: ')
        return Conta(numero, cliente)
    
def main(): # Cadastro de inputs do usuário
    print('Bem-vindo ao Banco GVM')

    print('\n--- Cadastro do Cliente ---')
    cliente = Cliente.criar_cliente()  # Vai puxar o método que está na classe Cliente
    print(cliente)

    print('\n--- Cadastro de Conta ---')
    conta = Conta.criar_conta(cliente)

    while True: 
         print(''' ================ MENU ================
            D = Depositar
            S = Sacar
            C = Consultar Saldo
            O = Sair 
         ''')

         opção = input('Digite a operação desejada: ').strip().lower()

         if opção == 'd':
                try:
                    valor = float(input('Digite o valor que você deseja depositar: '))
                    conta.depositar(valor)
                except ValueError:
                    print('ERRO! Por favor, insira um valor numérico válido.')


         elif opção == 's':
             try:
                valor = float(input('Digite o valor que você deseja sacar: '))
                conta.sacar(valor) # O valor aqui é o que vai cair no método la em cima entre os parenteses
             except ValueError:
                    print('ERRO! Por favor, insira um valor numérico válido.')  

         elif opção == 'c':
             conta.consultar_saldo()

         elif opção == 'o':
             print('Obrigado por usar nosso sistema. Volte sempre!')
             break
         else:
             print('Operação inválida. Tente novamente!')
        
if __name__ =='__main__':
    main()
         
             



        
         







 
 



