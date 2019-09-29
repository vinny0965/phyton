import bd , menu

def iniciar_sistema_cameras():
    while True:
        menu.menu_principal()
        op = input("Digite a opcao")
        if op == "2":
             print("Saindo do Sistema")
             break

        elif op == '1':
            cameraMarca = input("(((((Digite a marca da Câmera:))))")
            cameraIp= input("((((Digite o ip da câmera para rastrear:))))")
            localizar = input("digite o código de acesso:")
            cameras ={
                'cameraMarca' : cameraMarca,
                'cameraIp' : cameraIp,
                'localizar': localizar

            }

            bd.adicionar_camera(cameras)
            print('CAMERA CADRASTRADA COM SUCESSO<<<INICIANDO MONITORAMENTO>>>')