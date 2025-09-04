from locadora_classes import Veiculo
from locadora_classes import Moto
from locadora_classes import Carro
from locadora_classes import Caminhao

moto = Moto(1234, 'Honda', 'Vermelho', '2021', 'gasolina', '15,00')
moto.abastecer()
moto.empinar()
carro = Carro(2345, 'Porsche', 'Vermelho', '2025', 'hibrido', '100,00', 'automatico', 2)
carro.acelerar()
caminhao = Caminhao(3453, 'Mercedes', 'Azul', '2022', 'Diesel', '80,00', 3, 'Bau', 'manual', 200)
caminhao.freiar()
