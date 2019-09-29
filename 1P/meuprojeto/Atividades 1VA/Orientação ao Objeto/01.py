class televisor:
    volume=50
    canal=28

    def AlternarCanal(self,novocanal):
        if novocanal > 0 and novocanal <=600:
            self.canal = novocanal
        else:
            print("Canal Invalido")
    def AumentarVolume(self):
        if self.volume<100:
            self.volume +=1
        else:
            print("Volume Estourado")

    def DiminuirVolume():
        if volume > 0:
            self.volume -=1
        else:
            print("modo silencioso ativado")

    def VolumeAtual(self):
        print(f'Volume atual: (self.volume)')
    def CanalAtual(self):
        print(f'Canal atual: (self.canal)')