import enum

class Pagamento(enum.Enum):
    EmAberto = 1
    ParcialPago = 2
    Pago = 3

class Boleto:
    def __init__(self,cod_barras, v_boleto, v_pago, data1, data2, data3, pagamento):
        self.__cod_barras = cod_barras
        self.__v_boleto = v_boleto
        self.__v_pago = v_pago
        self.__data_emissao = data1
        self.__data_venci = data2
        self.__data_pagamento = data3
        self.__pagamento = pagamento
    
    def Pagar(self, valor):
        
