class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome   = nome
        self.idade  = idade
        self.peso   = peso
        self.altura = altura

    def comprimentar(self):
        print("Olá! Tudo bem?")

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, eu tenho aproximadamente {self.altura}cm de altura e eu peso {self.peso}kg")

pessoa1 = Pessoa("Eduardo", 24, 60, 165)

pessoa1.apresentar()

Pessoa.apresentar(pessoa1)