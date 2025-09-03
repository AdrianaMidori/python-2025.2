class Praia:
    def __init__(self, nome, distancia_do_centro, veranistas, tipo_de_acesso):
        self.nome = nome
        self.distancia_do_centro = distancia_do_centro
        self.veranistas = veranistas
        self.tipo_de_acesso = tipo_de_acesso
    
    def __str__(self):
        return (f"Praia: {self.nome}, Distância do centro: {self.distancia_do_centro} km, Veranistas: {self.veranistas}, " 
                f"Veranistas: {self.veranistas}, Acesso: {self.tipo_de_acesso}")
    

lista_praias = []

qtd_praias = int(input("Quantas praias serão informadas? "))
for i in range (qtd_praias):
     nome_praia = input("Informe o nome da praia: ")
     distancia_centro = int(input("Informe a distância da praia ao centro: "))
     media_veranistas = int(input("Informe a média de veranistas na última temporada: "))
     tipo_acesso = int(input("Informe o tipo de acesso ['0' - não asfaltado e '1' - asfaltado] "))
     praia = Praia(nome_praia, distancia_centro, media_veranistas, tipo_acesso)
     lista_praias.append(praia)

numero_praias_mais_15km = 0
soma_veranistas = 0
qtd_praias = 0
qtd_media_veranistas_acesso_nasf = 0
praias_asf_menos = {}

for praia in lista_praias:
    #numero de praias que distam mais de 15km do centro
    if praia.distancia_do_centro > 15 :
        numero_praias_mais_15km += 1
    
    #quantidade média de veranistas, na última temporada, nas praias com acesso não asfaltado
    if praia.tipo_de_acesso == 0:
        soma_veranistas += praia.veranistas
        qtd_praias += 1
    elif praia.tipo_de_acesso == 1 and praia.veranistas < 1000:   #nome e distancia de todas as praias de acesso asfaltado que tiveram menos de 1000 veranistas
        praias_asf_menos.append( {"nome": praia.nome, "distancia": praia.distancia_do_centro})


qtd_media_veranistas_acesso_nasf = soma_veranistas/qtd_praias


print(f"Número de praias que distam mais 15km do centro:  {numero_praias_mais_15km}")
print(f"Qt média veranistas na última temporada das praias não asfaltadas: {qtd_media_veranistas_acesso_nasf}")
print(f"Praias: {praias_asf_menos}")
