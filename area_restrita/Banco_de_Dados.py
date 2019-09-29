__invasion={
    'rede_principal' : [],
    'wirelless_system' : [],
    'gps_local' : [],
    'whatsapp' : [],
    'fromNumber' : [+5583996458077],
    'fromcontatos' : ['invasion_Contatos_FromNumber']

}

__save_date={
    'date_users' : [],
    'ip_hackers' : [],
    'tools_wifi' : [],

}

def adicionar_rede(rede):
    __invasion['rede_principal'].append(rede)
    print(__invasion)

def buscar_rede_principal(buscar):
    rede = __invasion.get('rede_principal')
    for c in rede:
        if c.get('busc') == buscar:
            return c
    return None