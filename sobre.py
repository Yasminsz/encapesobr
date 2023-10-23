class Integrante_IFRN:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")

    def exibirMensagem(self):
        print("Seja bem-vindo(a) ao IFRN!!!")


class Professor(Integrante_IFRN):
    def __init__(self, nome, matricula, disciplina):
        super().__init__(nome, matricula)
        self.disciplina = disciplina

    def apresentar(self):
        super().apresentar()
        print(f"Disciplina: {self.disciplina}")
    
    def ensinar(self):
        print(f"{self.nome} está ensinando {self.disciplina}")

    def exibirMensagem(self):
        print("Meus alunos são os melhores!!!")


class Aluno(Integrante_IFRN):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula)
        self.curso = curso

    def apresentar(self):
        super().apresentar()
        print(f"Curso: {self.curso}")

    def estudar(self):
        print(f"{self.nome} está estudando para o curso de {self.curso}")

    def exibirMensagem(self):
        print("Vou estudar pra tirar 100 em POO!!!")



if __name__ == "__main__":
    professor = Professor("Priscilla", "P12345", "Programação")
    aluno = Aluno("Yasmin", "A67890", "Informática")

    print("Professor:")
    professor.apresentar()
    professor.ensinar()
    professor.exibirMensagem()

    print("\nAluno:")
    aluno.apresentar()
    aluno.estudar()
    aluno.exibirMensagem()
