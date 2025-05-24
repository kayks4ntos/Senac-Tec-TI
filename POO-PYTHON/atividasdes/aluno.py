from dataclasses import dataclass
@dataclass
class Aluno:
    nome: str 
    idade: int
    nota: float
    def Media(self):
        return sum(self.nota) / len(self.nota)
    def situação(self):
        if self.Media() > 6:
            return "aprovado"
        elif self.Media() <6: 
            return "reprovado"
    def mostra_dados(self):
        print(f"nome: {self.nome}\n notas:{self.nota}\nmedia: {self.Media()}\n{self.situação()}")
notas = [9,3,7]
kayk = Aluno("kayk",12,notas)
kayk.Media()
kayk.situação()
kayk.mostra_dados()
