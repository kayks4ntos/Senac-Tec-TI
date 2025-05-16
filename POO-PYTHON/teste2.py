from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

@dataclass
class Estudante(Pessoa):
    curso: str


# Teste
aluno = Estudante("Kayk", 19, "Redes")
print(aluno.apresentar())
