class Pessoa:
    "Isto é uma classe nova chamada Pessoa"
    "Isto é uma nova string"

    idade = 24

    def saudacao(self):
        print("Olá mundo!")

print(Pessoa.idade)
print(Pessoa.saudacao)
print(Pessoa.__doc__)

eduardo = Pessoa()

print(eduardo.idade)

eduardo.saudacao()