class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self._nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string")

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if isinstance(nova_idade, int) and nova_idade >= 0:
            self._idade = nova_idade
        else:
            raise ValueError("A idade deve ser um número inteiro não negativo")


nome = input("Digite o nome da pessoa: ")
idade = input("Digite a idade da pessoa: ")


try:
    idade = int(idade)
except ValueError:
    print("A idade deve ser um número inteiro.")
    idade = 0

pessoa = Pessoa(nome, idade)


print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade}")
