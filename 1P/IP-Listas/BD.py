#cod, nome, sigla, status
__cursos=[]

#cod, nome, periodo, cod_curso
__disciplinas = []


#cpf, nome, periodo_entrada, cod_curso,
#LOGICA: 1 - semestre tem que ter o formato xxxx.x
#LOGICA: 2 - nome tem que ter nome e sobrenome
__alunos = []


def adicionar_curso(curso):
    __cursos.append(curso)


def buscar_curso_por_codigo(codigo):
    for c in __cursos:
        if c[0] == codigo:
            return c
    return None




def get_cursos():
    return __cursos.copy()


def adicionar_disciplina(displina):
    __disciplinas.append(displina)

def buscar_disciplina_por_codigo(codigo):
    for c in __disciplinas:
        if c[0] == codigo:
            return c
    return None



def buscar_disciplina_por_nome(nome):
    lista_temp=[]
    for c in __disciplinas:
        if str(c[1]).__contains__(nome):
            lista_temp.append(c)
    return lista_temp

def get_disciplinas():
    return __disciplinas.copy()