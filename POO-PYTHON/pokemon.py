from dataclasses import dataclass
print(f"{"-"*20}Começou o jogo de pokemon{"-"*20}")
@dataclass
class Pokemon:
    nome: str 
    tipo: str 
    nivel: int
    vivo: bool
    Vida: int = 100 
    

    def vida(self):
        self.Vida *= self.nivel
    def bater(self,outro_pokemon):
         self.morte()
         if self.vivo == False:
             print("ele esta morto")
         else:
            self.vida()
            dano = 10 * self.nivel
            outro_pokemon.Vida -=   dano 
            print(f"o pokemom {self.nome} bateu no {outro_pokemon.nome} e recebeu  {dano}")
        
    def exibir(self):
        self.morte()
        if self.vivo == False:
             print("ele esta morto")
        else:
            print(f"nome: {self.nome} \ntipo :{self.tipo} \nvida: {self.Vida}\nnivel: {self.nivel}")
    def morte(self):
        if self.Vida <= 0:
            print(f"pokemon {self.nome} morreu")
            self.vivo = False
pikachu = Pokemon("pikachu","eletrico",3,True)
kiterman = Pokemon("kiterman","fogo",1,True)
escolha = input("escolha o seu personagem\n[01] - pikachu\n[02] - kiterman\ndigite: ")
if escolha == "01":
    while True:
        print("-"*20)
        escolha2 = input("[01] -  escolha para bater\n[02] para exibir vida\n [10] escolha para sair\ndigite:")
        if escolha2 == "01":
            print("-"*20)
            pikachu.bater(kiterman)
        elif escolha2 == "02":
                print("-"*20)
                pikachu.exibir()
                print("-"*20)
                print(f"{"-"*20}inimigo{"-"*20}")
                kiterman.exibir()
        else:
            print("saiu")
            break

elif escolha == "02":
        while True:
            print("-"*20)
            escolha2 = input("[01] -  escolha para bater\n[02] para exibir vida\n [10] escolha para sair\ndigite:")
            if escolha2 == "01":
                print("-"*20)
                kiterman.bater(pikachu)
            elif escolha2 == "02":
                    print("-"*20)
                    kiterman.exibir()
                    print("-"*20)
                    print(f"{"-"*20}inimigo{"-"*20}")
                    pikachu.exibir()
            else:
                print("saiu")
                break


    