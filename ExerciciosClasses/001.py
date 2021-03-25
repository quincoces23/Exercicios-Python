# Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: troca Cor e mostra Cor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

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
