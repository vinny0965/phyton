# nome, cpf , telefone , sexo , idade
__clientes = []

# cliente_cpf, voo,

__voo = []

def adicionar_cliente(cliente):
    __clientes.append(cliente)

def telefone(telefone):
    __clientes.append(telefone)

def sexo(sexo):
    __clientes.append(sexo)

def idade(idade):
    __clientes.append(idade)

def buscar_cliente_por_cpf(cpf):
    for c in __clientes:
        if c[0] == cpf:
            return c
    return None

def get_clientes():
    return __clientes.copy()