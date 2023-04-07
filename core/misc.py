class Data:

    '''
    Cada objeto Data deve marcar uma data e hora do dia
    Ele interage com outros elementos de sua classe para gerar quanto tempo de passou
    '''

    mes = {
         0: "Vendemiário", #22 de setembro  a 21 de outubro
         1: "Brumário"   , #22 de outubro   a 20 de novembro
         2: "Frimário"   , #21 de novembro  a 20 de dezembro
        
         3: "Nivoso"     , #21 de dezembro  a 19 de janeiro
         4: "Pluvioso"   , #20 de janeiro   a 18 de fevereiro
         5: "Ventoso"    , #19 de fevereiro a 20 de março
        
         6: "Germinal"   , #21 de março     a 19 de abril
         7: "Floreal"    , #20 de abril     a 19 de maio
         8: "Prairial"   , #20 de maio      a 18 de junho

         9: "Messidor"   , #19 de junho     a 18 de julho
        10: "Termidor"   , #19 de julho     a 17 de agosto
        11: "Frutidor"   , #18 de agosto    a 17 de setembro.

        12: ""           , #18 de setembro a 21 de setembro (Sem-culotes) (inclui dia 366)
    }

    dia = {
        0: "Primeira-jornada",
        1: "Segunda-jornada",
        2: "Terceira-jornada",
        3: "Quarta-jornada",
        4: "Quinta-jornada",
        5: "Sexta-jornada",
        6: "Sétima-jornada",
        7: "Oitava-jornada",
        8: "Nona-jornada",
        9: "Décima-jornada",

    }

    decada = {
        0: "Primeira Década",
        1: "Segunda Década",
        2: "Terceira Década",
    }

    dia_extra = {
        0: "Dia da Virtude",
        1: "Dia do Engenho",
        2: "Dia do Trabalho",
        3: "Dia da Opinião",
        4: "Dia das Recompensas",
        5: "Dia da Revolução", # Anos bissextos
    }

    
    etapa = {
        0: "Penumbra"   , #( 0h as  3h)
        1: "Alvorada"   , #( 3h as  6h)
        2: "Aurora"     , #( 6h as  9h)
        3: "Manhã"      , #( 9h as 12h)
        4: "Tarde"      , #(12h as 15h)
        5: "Vespertino" , #(15h as 18h)
        6: "Noite"      , #(18h as 21h)
        7: "Crepúsculo" , #(21h as 24h)
    }


    def __init__(self, _ano=0, _mes=0, _dia=0, _etapa=0, _tique=0):
        '''
        self.tique - armazena quantas etapas se passaram desde o inicio do objeto
        self.ano   |
        self.mes   | 
        self.dia   - armazenam a data em formato de calendário tradicional, de 12 meses e 365 dias no ano
        self.etapa - registra qual etapa do dia é atualmente
        '''


        self.tique = _tique
        self.ano   = _ano
        self.mes   = _mes
        self.dia   = _dia
        self.etapa = _etapa


    def avancar_etapa(self, _etapas=1):
        self.tique  += _etapas
        self.etapa += _etapas
        if self.etapa > 7:
            self.avancar_dia(self.etapa // 8, False)
            self.etapa -= self.etapa // 8


    def avancar_dia(self, _dias=1, _avancar_tique=True):
        if _avancar_tique:
            self.tique += 8 * _dias
        
        self.dia += _dias

        while self.dia >= 30:
            while 30 <= self.dia and self.mes <= 12:
                self.mes += 1
                self.dia -= 30
            
            if self.dia >= 5 + int(self.ano % 4 == 0):
                self.dia -= 5 + int(self.ano % 4 == 0)
                self.mes = 0
                self.ano += 1


        if self.dia >= 5 + int(self.ano % 4 == 0) and self.mes == 12:
            self.dia -= 5 + int(self.ano % 4 == 0)
            self.mes  = 0
            self.ano += 1


    def get_data_curta(self):
        if self.mes != 12:
            return f"{(self.dia % 10) + 1}/{(self.dia // 10) + 1}/{(self.mes) + 1}/{self.ano}"

        return f"{self.dia}/13/{self.ano}"


    def get_data_extensa(self):
        if self.mes != 12:
            return f"{Data.dia[self.dia % 10]} da {Data.decada[self.dia // 10]} de {Data.mes[self.mes]}, {self.ano} EC"

        return f"{Data.dia_extra[self.dia]}, {self.ano} EC"