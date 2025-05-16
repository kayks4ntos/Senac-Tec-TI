from dataclasses import dataclass
import random

@dataclass
class Personagem:
    nome: str
    nivel: int
    ataque: int
    vida: int

    def atacar(self, inimigo):
        if self.vida <= 0:
            print(f"{self.nome} está derrotado e não pode atacar.")
            return False
        if inimigo.vida <= 0:
            print(f"{inimigo.nome} já está morto.")
            return False

        dano_base = self.ataque * self.nivel
        multiplicador = random.uniform(0.7, 1.0)
        dano_final = int(dano_base * multiplicador)

        chance_ataque = random.randint(1, 100)

        if chance_ataque % 2 == 0:
            inimigo.vida -= dano_final
            print(f"{self.nome} atacou {inimigo.nome} causando {dano_final} de dano!")
        else:
            print(f"{self.nome} tentou atacar {inimigo.nome}, mas errou!")

        # Inimigo reage ao ataque, se estiver vivo
        inimigo.verificar_vida(self)
        return True

    def mostrar_status(self):
        print(f"{self.nome} | Vida: {self.vida} | Ataque: {self.ataque} | Nível: {self.nivel}")

@dataclass
class Inimigo:
    nome: str
    nivel: int
    ataque: int
    vida: int

    def atacar(self, personagem):
        if self.vida <= 0:
            print(f"{self.nome} está morto e não pode atacar.")
            return False
        dano_base = self.ataque * self.nivel
        multiplicador = random.uniform(0.7, 1.0)
        dano_final = int(dano_base * multiplicador)
        chance_ataque = random.randint(1, 100)
        if chance_ataque % 2 == 0:
            personagem.vida -= dano_final
            print(f"{self.nome} contra-atacou {personagem.nome} causando {dano_final} de dano!")
        else:
            print(f"{self.nome} tentou contra-atacar, mas errou!")

    def verificar_vida(self, personagem):
        if self.vida <= 0:
            print(f"{self.nome} morreu.")
        else:
            self.atacar(personagem)


kayk = Personagem("kayk", 2, 20, 100)
globin = Inimigo("globin", 1, 10, 50)
dragão = Inimigo("dragão", 4, 10, 50)
paulista = Inimigo("paulista", 10, 10, 50)
kayk.mostrar_status()
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.atacar(aranha)
kayk.mostrar_status()



