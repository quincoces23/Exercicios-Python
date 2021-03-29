# Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: troca Cor e mostra Cor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self._cor = cor
        self._circunferencia = circunferencia
        self._material = material

    @property
    def cor(self):
        return self.cor

    @property
    def circunferencia(self):
        return self.circunferencia

    @property
    def material(self):
        return self.material

    @cor.setter
    def cor(self, cor):
        self.cor = cor

    @circunferencia.setter
    def circunferencia(self, circunferencia):
        self.circunferencia = circunferencia

    @material.setter
    def material(self, material):
        self.material = material

    def __str__(self):
        return f'{bola_kiko._cor} - {bola_kiko._circunferencia} - {bola_kiko._material}'


bola_kiko = Bola('Azul', 'quadrada', 'borracha')

lista_bolas = [bola_kiko]

for bolas in lista_bolas:
    print(f'{bolas}')
