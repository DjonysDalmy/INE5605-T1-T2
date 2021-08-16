from limite.tela_sistema import TelaSistema
from controle.controlador_curso import ControladorCurso
from controle.controlador_disciplina import ControladorDisciplina
from controle.controlador_professor import ControladorProfessor
from controle.controlador_aluno import ControladorAluno
from controle.controlador_atividade import ControladorAtividade

class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_curso = ControladorCurso(self)
        self.__controlador_disciplina = ControladorDisciplina(self)
        self.__controlador_professor = ControladorProfessor(self)
        self.__controlador_aluno= ControladorAluno(self)
        self.__controlador_atividade = ControladorAtividade(self)

    def inicializa_sistema(self):
        self.abre_tela()

    def curso(self):
        self.__controlador_curso.abre_tela()

    def professor(self):
        self.__controlador_professor.abre_tela()

    def disciplina(self):
        self.__controlador_disciplina.abre_tela()

    def aluno(self):
        self.__controlador_aluno.abre_tela()

    def atividade(self):
        self.__controlador_atividade.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.curso, 2: self.professor, 3: self.disciplina, 4: self.aluno,5: self.atividade, 0:self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()