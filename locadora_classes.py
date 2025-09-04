class Veiculo():
    def __init__(self, chassi, marca, cor, ano_fabricacao, tipo_combustivel, preco_diaria):
        self.chassi = chassi
        self.marca = marca
        self.cor = cor
        self.ano_fabricacao = ano_fabricacao
        self.tipo_combustivel = tipo_combustivel
        self.preco_diaria = preco_diaria

    def acelerar(self):
        print('Veículo acelerando')

    def freiar(self):
        print('Veículo freiando')
    
    def abastecer(self):
        print('Veículo abastecendo')


class Moto(Veiculo):
    def empinar(self):
        print('Moto empinando')

class Carro(Veiculo):
    def __init__(self, chassi, marca, cor, ano_fabricacao, tipo_combustivel, preco_diaria, tipo_cambio, quant_lugares, potencia_motor):
        super().__init__(chassi, marca, cor, ano_fabricacao, tipo_combustivel, preco_diaria)
        self.tipo_cambio = tipo_cambio
        self.quant_lugares = quant_lugares
        self.potencia_motor = potencia_motor

class Caminhao(Veiculo):
    def __init__(self, chassi, marca, cor, ano_fabricacao, tipo_combustivel, preco_diaria, quant_eixos, tipo_carroceria, tipo_cambio, capacidade_carga):
        super().__init__(chassi, marca, cor, ano_fabricacao, tipo_combustivel, preco_diaria)    
        self.quant_eixos = quant_eixos
        self.tipo_carroceria = tipo_carroceria
        self.tipo_cambio = tipo_cambio
        self.capacidade_carga = capacidade_carga
