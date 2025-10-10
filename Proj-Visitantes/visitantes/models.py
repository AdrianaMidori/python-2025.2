from django.db import models

class Visitante(models.Model):
    nome_completo = models.CharField (verbose_name = 'Nome completo',
                                      max_length = 100)
    
    cpf = models.CharField (verbose_name = 'CPF',
                            max_length = 11,
                            unique = True)
    
    data_nascimento = models.DateField(verbose_name = 'Data de Nascimento',
                                       auto_now = False,
                                       auto_now_add = False,
                                       help_text="Insira a data no formato dd-mm-aaaa"
                                       )
    
    numero_casa = models.PositiveSmallIntegerField (verbose_name = 'Número da casa a ser visitada'
                                 )
    
    placa_do_veiculo = models.CharField (verbose_name = 'Placa do veículo',
                                         max_length = 7,
                                         blank = True,
                                         null = True)
    
    horario_chegada = models.DateTimeField(verbose_name = 'Horário de Chegada na Portaria',
                                              auto_now_add = True
                                            )
    
    horario_de_saida = models.DateTimeField(verbose_name = 'Horário de saída do condomínio',
                                              auto_now = False,
                                              blank = True,
                                              null = True
                                            )
    horario_de_autorizacao = models.DateTimeField(verbose_name = 'Horário de autorização de Entrada',
                                              auto_now = False,
                                              blank = True,
                                              null = True
                                            )
    morador_responsavel = models.CharField (verbose_name = 'Nome do morador responsável por autorizar a entrada',
                                      max_length = 50,
                                      blank = True)
    
    registrado_por = models.ForeignKey(
                                    'porteiros.Porteiro',
                                    verbose_name = 'Porteiro responsável pelo registro',
                                    on_delete = models.PROTECT
                                    )
    
    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        db_table = 'visitante'

    def __str__(self):
        return self.nome_completo

    
