'''cpf = '41361568801'

print(cpf[:3])
print(cpf[3:6])
print(cpf[6:9])
print(cpf[9:11])'''

from models.cliente import Cliente
from models.conta import Conta


cl1: Cliente = Cliente('Bruno Rodrigues','41361568801','bruno77_sr@gmail.com','27/06/1997')
cl2: Cliente = Cliente('Talpa Ator','58256668801','Talpa@gmail.com','02/06/1988')


print(cl1)
print("*********")
print(cl2)


conta1 = Conta(cl1)
conta2 = Conta(cl2)

'''print(conta1)
print("*********")
print(conta2)'''

cont = 1

a = 'cl'

var = a + str(cont)

print(var)


'''def conta_destino():
    numero_d: int = int(input('Digite número da conta de destino: '))

    conta_d: Conta = buscar_conta_por_numero(numero_d)
        if conta_d:
            pass
        else:
            print(f'Não foi encontrada a conta com o número {conta_d}')
        return conta_d'''

print("hello" 'word' * 2)