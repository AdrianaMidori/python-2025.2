from django.db import models

class Porteiro(models.Model):
    nome_completo = models.CharField (verbose_name = 'Nome completo',
                                      max_length = 100)
    cpf = models.CharField (verbose_name = 'CPF',
                            max_length = 11,
                            unique = True)
    telefone = models.CharField (verbose_name = 'Telefone para Contato',
                                 max_length = 11)
    data_nascimento = models.DateField(verbose_name = 'Data de Nascimento',
                                       auto_now = False,
                                       auto_now_add = False,
                                       help_text="Insira a data no formato dd-mm-aaaa"
                                       )
    
    #Relacionando a "tabela" porteiro com a usuario através de uma ligação um para um, 
    #Um porteiro terá apenas um correspondente no usuário
    #PROTECT, porque caso o usuário(pai) seja deletado o porteiro também seja deletado
    #Caso o porteiro seja deletado não será necessário deletar o usuário
    usuario = models.OneToOneField(
        'usuarios.Usuario',
        verbose_name = 'Usuário',
        on_delete = models.PROTECT

    )
    
    class Meta:
        verbose_name = 'Porteiro'
        verbose_name_plural = 'Porteiros'
        db_table = 'porteiro'
    
    def __str__(self):
            return self.nome_completo
