#cliente, nome , cpf , sexo , telefone
__clientes = []

#cod , cliente ,valor_total_contrato, quantidade_parcelas
__contratos = []

#cod , contrato , valor_parcela , situacao, data vencimento
__boletos = []

def adicionar_cliente(cliente):
    __clientes.append(cliente)

def buscar_por_cpf(cpf):
    for c in __clientes:
        if c[0] == cpf:
            return c
    return None

def sexo_do_cliente(sexo):
    __clientes.append(sexo)

def telefone_do_cliente(telefone):
    __clientes.append(telefone)

def get_clientes():
    return __clientes.copy()

def adicionar_contrato(contrato):
    __contratos.append(contrato)

def buscar_contrato_por_codigo(codigo):
    for c in __contratos:
        if c[0] == codigo:
            return c
    return None

def get_contratos():
    return __contratos.copy()

def adicionar_boleto(boleto):
    __boletos.append(boleto)

def buscar_boleto_por_codigo(codigo):
    for c in __boletos:
        if c[0] == codigo:
            return c
    return None

def get_boletos():
    return __boletos.copy()



