from dataclasses import dataclass
from abc import ABC, abstractmethod
@dataclass
class Pagamento(ABC):
    valor : float
    @abstractmethod
    def pagar(self):
        pass
class pix(Pagamento):
    def pagar(self):
        print(f"pagar via pix no valor de {self.valor:.2f}")
class cartao_credito(Pagamento):
    def pagar(self):
        print(f"pagar via cretido no valor de {self.valor:.2f}")

class debito(Pagamento):
    def pagar(self):
        print(f"pagar via debito no valor de {self.valor:.2f}")
pagamento = [
    pix(12.6),
    cartao_credito(23.8),
    debito(45.4)
]
for x in pagamento:
    x.pagar()







