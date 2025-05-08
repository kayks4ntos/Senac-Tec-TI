from dataclasses import dataclass
import random
@dataclass
class Inimigo:
    nome : str 
    nivel : int
    ataque : int
    vida : int 
    def atacar(self,personagem):
        if self.vida <= 0:
            print("mostro morto")
            return False
        
        self.ataque *= self.nivel 
        personagem.vida -= self.ataque
    def defesa(self,personagem):
        if self.vida <= 0:
            print("mostro morto")
            return False
        personagem.ataque -= self.nivel * 2
aranha = Inimigo("aranha",1,10,50)
goblin = Inimigo("goblin",20,10,250)
pualista = Inimigo("paulista",99,10,1000)





