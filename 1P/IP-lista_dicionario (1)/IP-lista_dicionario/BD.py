#cod, nome, sigla, status
__banco_de_dados = {
    'cursos': [],
    'disciplinas': [],
    'alunos': {},
}

__cursos=[]

#cod, nome, periodo, cod_curso
__disciplinas = []


#cpf, nome, periodo_entrada, cod_curso,
#LOGICA: 1 - semestre tem que ter o formato xxxx.x
#LOGICA: 2 - nome tem que ter nome e sobrenome
__alunos = []


def adicionar_curso(curso):
    __banco_de_dados['cursos'].append(curso)
    print(__banco_de_dados)

def buscar_curso_por_codigo(codigo):
    cursos = __banco_de_dados.get('cursos')
    for c in cursos:
        if c.get('cod') == codigo:
            return c
    return None




def get_cursos():
    return __banco_de_dados.get('cursos').copy()


def adicionar_disciplina(disciplina):
    __banco_de_dados['disciplinas'].append(disciplina)
    print(__banco_de_dados)


def buscar_disciplina_por_codigo(codigo):
    disciplinas = __banco_de_dados.get('disciplinas')
    for c in disciplinas:
        if c.get('cod') == codigo:
            return c
    return None



def buscar_disciplina_por_nome(nome):
    disciplinas = __banco_de_dados.get('disciplinas')
    for c in disciplinas:
        if c.get('nome') == nome:
            return c
    return None

def get_disciplinas():
    return __banco_de_dados.get('disciplinas').copy()