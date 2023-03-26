class Campanha:
    '''
    Parâmetros:
        campanha = STR  ex:(a, b, c)
        cpc = FLOAT     ex: (0.05)
        impr = INT      ex: (1234324)
        ctr = FLOAT     ex: (0.89)
        tx =  FLOAT     ex: (0,90)
        ROI = FLOAT/INT ex: (12.5) ou (50)
        vendas = INT    ex: (1000)
    '''
    def __init__(self, campanha, cpc, impr, ctr, tx, roi, vendas):

        self.nome = campanha.upper()
        self.cpc = float(cpc)
        self.impressoes_diarias = float(impr)
        self.ctr = float(ctr)/100
        self.tx = float(tx)/100
        self.roi = float(roi)/100
        self.vendas_dia = float(vendas)
        self.cliques_diarios = self.impressoes_diarias * self.ctr
        self.custo_diario = self.cliques_diarios * self.cpc
        self.lucro_diario = self.roi * self.custo_diario
        self._cpa = self.custo_diario / self.vendas_dia
        self.receita_diaria = self.lucro_diario + (self._cpa*self.vendas_dia)
        self.receita_mensal = self.receita_diaria * 30
        self._rpa = self.receita_diaria / self.vendas_dia
        self.lucro_mensal = self.lucro_diario * 30
        
    def crise(self):
        
        self.novo_roi = 1
        self.novo_rpa = 10
        self.nova_receita_diaria = (self.novo_rpa * self.vendas_dia)
        self.novo_custo_diario = self.nova_receita_diaria / 2
        self.novo_cpc = self.novo_custo_diario / (self.impressoes_diarias * self.ctr)
        self.novo_lucro_mensal = (self.nova_receita_diaria - self.novo_custo_diario) * 30
        return print(f'\n\
                        \nNovo CPC da campanha *{self.nome}* deve ser {self.novo_cpc:,.2f}\
                        \nO novo lucro mensal deverá ser R$ {self.novo_lucro_mensal:,.2f}')    
    def __str__(self):

        self.dados = f'\n\
                    \nOs dados da campanha *{self.nome}* são:\
                    \nCpa: R$ {self._cpa:,.2f}; \
                    \nRpa: R$ {self._rpa:,.2f};\
                    \nCliques Diários: {self.cliques_diarios:,.0f};\
                    \nLucro Diário R$ {self.lucro_diario:,.2f};\
                    \nLucro Mensal: R$ {self.lucro_mensal:,.2f};\
                    \nReceita Diária: R$ {self.receita_diaria:,.2f}\
                    \nReceita Mensal: R$ {self.receita_mensal:,.2f};'
        return self.dados
    