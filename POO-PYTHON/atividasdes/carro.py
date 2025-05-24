from dataclasses import dataclass
@dataclass
class Carro:
    marca: str 
    modelo: str 
    ano : str 
    velocidade: int = 0 
    def acelerar(self):
        self.velocidade += 10
    def frear(self):
         if self.velocidade <=0:
            return False 
         self.velocidade -=10
    def mostrar_dados(self):
        print(f"marca: {self.marca}\nmodelo:{self.modelo}\nAno:{self.ano}\nVelocidade:{self.velocidade} km/h")
chevrole = Carro("cherole","camaro","2020",)
chevrole.frear()
print(f"{"-"*20}dados do veiculo{"-"*20}")
chevrole.mostrar_dados()

     