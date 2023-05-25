#Exercício E2: criar três classes (1 herança, 1 agregação ou composição e 1 classe simples) com atributos e métodos;
#a) elaborar código que inspeciona as classes o melhor possível: exibir atributos e métodos, executar métodos, etc
#b) ao terminar, compartilhar o link de acesso a seu código (preferência: repositório)
#c) baixar os códigos de outros colegas, tentar usar seu código de inspeção para exibir informações dos códigos dos outros

# Classe com herança
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Gato(Animal):
    def fazer_som(self):
        print("O gato faz 'Miau'!")

# Classe com agregação
class Carro:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

# Classe simples
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando instâncias das classes
gato = Gato("Bola")
carro = Carro("Toyota", Motor("V8"))
pessoa = Pessoa("João", 30)

# Inspecionando a classe Gato
print("=== Classe Gato ===")
print("Atributos:")
print(dir(gato))
print("Métodos:")
print([method for method in dir(gato) if callable(getattr(gato, method))])

# Inspecionando a classe Carro
print("=== Classe Carro ===")
print("Atributos:")
print(dir(carro))
print("Métodos:")
print([method for method in dir(carro) if callable(getattr(carro, method))])

# Inspecionando a classe Pessoa
print("=== Classe Pessoa ===")
print("Atributos:")
print(dir(pessoa))
print("Métodos:")
print([method for method in dir(pessoa) if callable(getattr(pessoa, method))])
