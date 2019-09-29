class No(object):
    def __init__(self):
        self.__dado = None
        self.__proximo = None

    def set_Dado(self, dado):
        self.__dado = dado

    def get_Dado(self):
        return self.__dado

    def set_Proximo(self, proximo):
        self.__proximo = proximo

    def get_Proximo(self):
        return self.__proximo

    def to_String(self):
        return "Dado: " + self.get_Dado()