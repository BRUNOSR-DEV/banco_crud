from models.cliente import Cliente
import MySQLdb
from utils.helper import formata_float_str_moeda
from utils.helper import conectar,desconectar,str_para_date

class Conta:


    def __init__(self:object, cliente: Cliente) -> None:
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0
        self.__limite: float = 100 #Limite seria uma especie de LIS, empréstimo
        self.__saldo_total: float = self._calcula_saldo_total
        self.__num_conta = criar_num_conta()
        

    @property
    def numero(self)-> int:
        return self.__numero
    
    @property
    def cliente(self)-> Cliente:
        return self.__cliente
    
    @property
    def saldo_total(self):
        return self.__saldo_total
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self:object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self:object, valor: float) -> None:
        self.__limite = valor
    
    @property
    def _calcula_saldo_total(self) -> float:
        return self.saldo + self.limite
    
    @saldo_total.setter
    def saldo_total(self:object, valor:float) -> None:
        self.__saldo_total = valor

    def __str__(self:object) -> str:
        return f'Número da conta: {self.numero} \nCliente: {self.cliente.nome} \nValor em conta: {formata_float_str_moeda(self.saldo)}\nLimite: {formata_float_str_moeda(self.limite)}'


    def depositar(self,valor:float) -> str:
        if valor > 0:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total

            if self.saldo > 0:
                self.limite = 100
            else:
                self.limite = self.limite + valor

            return f'Operação bem sucedida!\nSaldo em Conta: {formata_float_str_moeda(self.saldo)}\nLimite da Conta: {formata_float_str_moeda(self.limite)}'
        else:
            print('Erro! Tente novamente!')


    def sacar(self,valor:float) -> str:

        if valor > 0 and self.saldo_total >= valor:

            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total

                return f'Saque realizado com sucesso.\n Saldo em Conta: {formata_float_str_moeda(self.saldo)}\nLimite da Conta: {formata_float_str_moeda(self.limite)}'
            else:
                restante: float = self.saldo - valor
                verifica_limite = self.limite + restante

                if verifica_limite >= 0:
                    self.saldo = 0
                    self.limite = self.limite + restante
                    self.saldo_total = self._calcula_saldo_total
                    return (f'Saque realizado! Valor total da conta: {formata_float_str_moeda(self.saldo_total)}')
                else:
                    return (f'Erro! Valor do limite insuficiente! \n Valor total da conta: {formata_float_str_moeda(self.saldo_total)}')
        else:
            return ('Saque não realizado.\nTente novamente!')


    def tranferir(self: object ,destino:object, valor: float) -> str:


        if valor > 0 and self.saldo_total >= valor:
            if self.saldo > valor:
                destino.depositar(valor)
                self.saldo = self.saldo - valor
                #self.saldo_total = self._calcula_saldo_total

                return f' O valor de {formata_float_str_moeda(valor)} foi tranferido com sucesso\n Saldo em Conta: {formata_float_str_moeda(self.saldo)}\nLimite da Conta: {formata_float_str_moeda(self.limite)}'
            else:
                restante: float = valor - self.saldo
                self.saldo = 0
                if self.limite > restante:
                    self.limite = self.limite - restante
                    self.saldo = self.saldo - restante
                    destino.depositar(valor)

                    #self.saldo_total = self._calcula_saldo_total

                return f' O valor de {formata_float_str_moeda(valor)} foi tranferido com sucesso\n Saldo em Conta: {formata_float_str_moeda(self.saldo)}\nLimite da Conta: {formata_float_str_moeda(self.limite)} '
        else:
            print('Erro! Tente novamente!')

    

def criar_num_conta():

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM contas')
        contas = cursor.fetchall()

        num_conta = 1001

        for conta in contas:
            if conta == num_conta:
                num_conta = num_conta + 1
            else:
                return num_conta

def gravar_dados_conta(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO contas (num_conta, saldo, limite) VALUES ({criar_num_conta()},{self.saldo},{self.limite}")
        conn.commit()