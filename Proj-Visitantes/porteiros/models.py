from django.db import models

class Porteiro():
    nome_completo = models.TextField (verbose_name = 'Nome completo',
                                      max_length = 100)
    cpf = models.TextField (verbose_name = 'CPF',
                            unique = True)
    telefone = models.TextField (verbose_name = 'Telefone',
                                 max_length = 12)
    data_nascimento = models.DateField(verbose_name = 'Data de nascimento',
                                       help_text="Insira a data no formato dd-mm-aaaa"
                                       )
    
    USER_NAME_FIELD = 'cpf'

    class Meta:
        verbose_name = 'Porteiro'
        verbose_name_plural = 'Porteiros'
        db_table = 'porteiro'

        def __str__(self):
            return self.cpf
