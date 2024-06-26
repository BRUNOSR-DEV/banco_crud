from models.conta import Conta
from datetime import date, datetime
from datetime import date
from datetime import datetime
from utils.helper import conectar,desconectar,str_para_date


def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%y') #fUNCIONA BEM

def str_para_date(data: str) -> date:
    return datetime.strptime(date, '%d/%m/%y') # NÃO ESTÁ FUNCIONANDO

def formata_float_str_moeda(valor:float) -> str:
    return f'R${valor:,.2f}'

def formata_cpf_str(cpf: str) -> str:
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'


class Cliente:

    contador: int = 101

    def __init__(self, nome: str,cpf:str,email: str, data_nascimento: str) -> None:

        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: date = data_nascimento
        self.__data_cadastro: date =  datetime.now()
        self.__gravar_dados = gravar_dados_cliente()
        

    @property
    def nome(self:object) -> str:
        return self.__nome
    @property
    def email(self:object) -> str:
        return self.__email
    @property
    def cpf(self:object) -> str:
        return self.__cpf
    @property
    def data_nascimento(self:object) -> str:
        return (self.__data_nascimento)
    @property
    def data_cadastro(self:object) -> str:
        return date_para_str(self.__data_cadastro)
    @property
    def gravar_dados(self):
        return gravar_dados_cliente()
    

    def __str__(self) -> str:
        return f'Nome:{self.nome} \nData de Nascimento:{self.data_nascimento} \nCadastro: {self.data_cadastro} \nCPF: {formata_cpf_str(self.cpf)}'

def gravar_dados_cliente(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO clientes (nome, email, cpf, data_nascimento, data_cadastro, id_contas) VALUES ('{self.nome}','{self.email}','{self.cpf}',{str_para_date(self.data_nascimento)},{Cliente.__data_cadastro},{Conta.num_id()})")

        conn.commit()

        desconectar(conn)