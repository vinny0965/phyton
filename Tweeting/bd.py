__banco_de_dados = {
    'cameras' : [],
}

__cameras = []

def adicionar_camera(camera):
    __banco_de_dados['cameras'].append(camera)
    print(__banco_de_dados)