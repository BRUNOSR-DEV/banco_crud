import MySQLdb

from datetime import date
from datetime import datetime



def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%y')

def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%y')

def formata_float_str_moeda(valor:float) -> str:
    return f'R${valor:,.2f}'

def formata_cpf_str(cpf: str) -> str:

    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'



def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = MySQLdb.connect(
            db= 'proj_banco',
            host= 'localhost',
            user= 'hey',
            passwd= 'boney',
        )
        return conn

    except MySQLdb.Error as e:
        print(f'Erro na conexão ao MySql Server: {e}')


def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn= conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()

    if len(clientes) > 0:
        print('listando clientes...')
        print('***************')
        for cliente in clientes:
            print('--------------------------')
            print(f'Id: {cliente[0]}')
            print(f'nome: {cliente[1]}')
            print(f'E-mail: {cliente[2]}')
            print(f'CPF: {cliente[3]}')
            print(f'Data nascimento: {date_para_str(cliente[4])}')
            print(f'Data de cadastro: {date_para_str(cliente[5])}')
            print(f'ID da conta: {cliente[6]}')
            print('--------------------------')
    else:
        print('Não existe produtos cadastrados.')
    desconectar(conn)








'''ret = (date_para_str(datetime.now()))
print(str_para_date(ret))

print(formata_cpf_str('41361568801'))'''