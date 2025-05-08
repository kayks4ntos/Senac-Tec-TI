from dataclasses import dataclass
@dataclass
class Produto:
    nome : str 
    preco :float
    quantidade : int = 0 
    def comprar(self,qtd):
        self.quantidade += qtd
        print(f"seu estoque recebeu{qtd}")
        print("-"*20)
    def vender(self,qtd):
        self.quantidade -= qtd 
        print(f"seu estoque perdeu{qtd}")
        print("-"*20)
    def mostra_dados(self):
        print(f"nome: {self.nome}\nestoque: {self.quantidade}")
macarrao = Produto("macarrão",3.5)
macarrao.comprar(100)
macarrao.vender(10)
macarrao.mostra_dados() 