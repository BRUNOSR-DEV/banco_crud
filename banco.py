from typing import List
from time import sleep
import MySQLdb
from models.cliente import Cliente, gravar_dados_cliente
from models.conta import Conta
from utils.helper import conectar,desconectar,str_para_date
from datetime import datetime


#Clientes e Contas pré definidos
cl1: Cliente = Cliente('Talpa Ator','12456852546','talpa@gmail.com','12/10/1950')
cl2: Cliente = Cliente('Flegma Lucios','42525685202','flegma@gmail.com','12/10/1970')

ct1: Conta = Conta(cl1)
ct2: Conta = Conta(cl2)

contas: List[Conta] = []

contas.append(ct1)
contas.append(ct2)


def main() -> None:
    menu()


def menu()-> None:
    print("========================")
    print(" Bem Vindo ao Banco BR")
    print("========================")

    '''op = 's'
    while op == 's' or op == 'S':'''
    
    print('[1] Criar Conta\n[2] Efetuar Saque\n[3] Efetuar Deposito\n[4] Efetuar Transferência\n[5] Listar Contas\n[6] Sair')

    resp = int(input('Digite um número correspondente: '))

    if resp == 1:
        criar_conta()
        exit()
    elif resp == 2:
        saque()
        exit()
    elif resp == 3:
        deposito()
        exit()
    elif resp == 4:
        tranferencia()
        exit()
    elif resp == 5:
        listar_contas()
        exit()
    elif resp == 6:
        print('Volte sempre! ')
        sleep(2)
        exit(0)
    else:
        print('Digite um número válido')
        sleep(3)
        menu()
        exit()


def criar_conta()-> None:

    print("========================")
    print("   Criação de Contas")
    print("========================")

    print('Preencha os dados a baixo')

    

    nome = input('Nome: ')
    cpf = input('CPF: ')
    email = input('E-mail: ')
    dt_nascimento = input('Data de Nascimento: ')

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO clientes (nome, email,  cpf, data_nascimento, data_cadastro, id_contas ) VALUES ('{nome}','{email}','{cpf}',{str_para_date(dt_nascimento)},{datetime.now()})")
    

    conn.commit()
    

    #contas.append(conta)

    
    
    
    

    print('Conta foi criada com sucesso.')
    print('Dados da conta:')
    print('--------------')
    print(conta)
    sleep(1)
    menu()


def saque()-> None:
    print('===============================')
    print('        Área de Saque')
    print('===============================')

    if len(contas) > 0:
        numero: int = int(input('Digite o número da conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor_saque = float(input('Informe o valor: ' ))

            print(conta.sacar(valor_saque))
        else:
            print(f'Não foi encontrada a conta com o número {numero}')
            print('Tente novamente!')
            sleep(2)
            saque()

    else:
        print('Não a contas registradas! ')
    sleep(5)
    menu()


def deposito()-> None:
    print('===============================')
    print('    ÁREA DE Deposito')
    print('===============================')

    if len(contas) > 0:
        numero: int = int(input('Digite o número da conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor_deposito = float(input('Informe o valor: ' ))

            print(conta.depositar(valor_deposito))
        else:
            print(f'Não foi encontrada a conta com o número {numero}')
            print('Tente novamente!')
            sleep(2)
            deposito()
    else:
        print('Não a contas registradas! ')
    sleep(5)
    menu()


def tranferencia()-> None:
    print('===============================')
    print('    ÁREA DE TRANFERENCIA')
    print('===============================')

    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da conta: ')) #informe o número da conta que irá fazer a tranferência.

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
                numero_d: int = int(input('Digite número da conta de destino: '))

                conta_d: Conta = buscar_conta_por_numero(numero_d)
          
                if conta_d:
                    valor_tras: float = float(input('Informe o valor: '))

                    print(conta_o.tranferir(conta_d,valor_tras))

                else:
                    print(f'Não foi encontrada a conta com o número {numero_d}')
                    print('Tente novamente!')
                    tranferencia() 
        else:
            print(f'Não foi encontrada a conta com o número {numero_o}')
            print('Tente novamente!')
            tranferencia()

    else:
        print('Não a contas registradas! ')
    sleep(5)
    menu()


def listar_contas()-> None:

    if len(contas) > 0:
        for conta in contas:
            print(conta)
            print('=========================')
            sleep(2)
    else:
        print('Não a contas registradas! ')
    sleep(5)
    menu()


def buscar_conta_por_numero(numero:int) -> Conta:
        c: Conta = None

        if len(contas) > 0:
             for conta in contas:
                if conta.numero == numero:
                    c = conta

       
        return c






if __name__ == '__main__':
    main()